#!/usr/bin/env python3

from __future__ import annotations

import argparse
import os
import platform
import shutil
import subprocess
import sys
import unicodedata
from dataclasses import dataclass
from typing import Callable, Iterable

MENU_WIDTH = 118
MENU_INNER_WIDTH = MENU_WIDTH - 4
MENU_COLUMNS = 2
MENU_COLUMN_GAP = 2

CATEGORY_COLORS = {
    "Update & repair": "green",
    "Package lab": "cyan",
    "Cleanup crew": "yellow",
    "System dashboard": "blue",
    "Network tools": "magenta",
    "Logs & services": "white",
    "Power deck": "red",
}

RESET = "\033[0m"
COLORS = {
    "black": "\033[30m",
    "red": "\033[31m",
    "green": "\033[32m",
    "yellow": "\033[33m",
    "blue": "\033[34m",
    "magenta": "\033[35m",
    "cyan": "\033[36m",
    "white": "\033[37m",
    "bold": "\033[1m",
}

ART_LINES = [
    r"   __  __          __      __                      ",
    r"  / / / /___  ____/ /___ _/ /____  ____ ___  ___  ",
    r" / / / / __ \/ __  / __ `/ __/ _ \/ __ `__ \/ _ \ ",
    r"/ /_/ / /_/ / /_/ / /_/ / /_/  __/ / / / / /  __/ ",
    r"\__,_/ .___/\__,_/\__,_/\__/\___/_/ /_/ /_/\___/  ",
    r"     /_/                                           ",
]
TAGLINE = "Debian maintenance command center • by WastelandSYS"


@dataclass(frozen=True)
class MenuItem:
    number: str
    label: str
    action: Callable[[], None]
    category: str
    icon: str
    description: str


def colorize(text: str, color: str) -> str:
    """Return text wrapped in an ANSI color when stdout is a terminal."""
    if not sys.stdout.isatty():
        return text
    return f"{COLORS.get(color, '')}{text}{RESET}"


def colorize_parts(parts: Iterable[tuple[str, str]]) -> str:
    """Return multiple colorized text segments as one string."""
    return "".join(colorize(text, color) for text, color in parts)


def print_color(text: str, color: str) -> None:
    """Print text with color when supported."""
    print(colorize(text, color))


def clear_screen() -> None:
    """Clear the terminal screen."""
    if sys.stdout.isatty():
        os.system("clear" if os.name == "posix" else "cls")


def pause() -> None:
    """Pause before returning to the menu in interactive terminals."""
    if sys.stdin.isatty():
        input(colorize("\n↩ Press Enter to return to the command center...", "yellow"))


def find_command(*names: str) -> str | None:
    """Return the first executable found on PATH."""
    for name in names:
        path = shutil.which(name)
        if path:
            return path
    return None


def require_command(*names: str) -> str:
    """Return an executable path or stop with a helpful message."""
    command = find_command(*names)
    if command:
        return command
    print_color(f"Missing required command: one of {', '.join(names)}", "red")
    sys.exit(1)


def needs_sudo(command: str) -> bool:
    """Return whether a command should be run through sudo."""
    return os.name == "posix" and os.geteuid() != 0 and os.path.basename(command) in {
        "apt",
        "apt-get",
        "apt-mark",
        "dpkg",
        "reboot",
        "shutdown",
    }


def run_command(command: Iterable[str], *, check: bool = False) -> subprocess.CompletedProcess[str]:
    """Run a command safely without invoking a shell."""
    command_list = list(command)
    if not command_list:
        raise ValueError("command cannot be empty")

    if needs_sudo(command_list[0]):
        sudo = require_command("sudo")
        command_list.insert(0, sudo)

    print_color(f"\n❯ {' '.join(command_list)}", "magenta")
    result = subprocess.run(command_list, check=False, text=True)
    if check and result.returncode != 0:
        raise subprocess.CalledProcessError(result.returncode, command_list)
    if result.returncode != 0:
        print_color(f"Command exited with status {result.returncode}.", "red")
    return result


def run_sequence(commands: Iterable[Iterable[str]]) -> bool:
    """Run commands in order and stop at the first failure."""
    for command in commands:
        result = run_command(command)
        if result.returncode != 0:
            return False
    return True


def apt_get(*args: str) -> subprocess.CompletedProcess[str]:
    """Run apt-get with safe defaults."""
    return run_command([require_command("apt-get"), *args])


def apt(*args: str) -> subprocess.CompletedProcess[str]:
    """Run apt with safe defaults."""
    return run_command([require_command("apt"), *args])


def apt_mark(*args: str) -> subprocess.CompletedProcess[str]:
    """Run apt-mark with safe defaults."""
    return run_command([require_command("apt-mark"), *args])


def prompt_package(prompt: str) -> str | None:
    """Prompt for a package name and allow the user to go back."""
    package_name = input(colorize(prompt, "yellow")).strip()
    if not package_name or package_name.lower() in {"b", "back"}:
        return None
    return package_name


def run_update() -> None:
    apt_get("update")


def refresh_package_lists() -> None:
    run_update()
    pause()


def regular_upgrade() -> None:
    apt_get("upgrade")
    pause()


def distribution_upgrade() -> None:
    apt_get("dist-upgrade")
    pause()


def full_upgrade() -> None:
    apt_get("full-upgrade")
    pause()


def simulate_upgrade() -> None:
    apt_get("--simulate", "upgrade")
    pause()


def fix_broken_packages() -> None:
    apt_get("install", "--fix-broken")
    pause()


def configure_pending_packages() -> None:
    run_command([require_command("dpkg"), "--configure", "-a"])
    pause()


def upgrade_specific_package() -> None:
    while True:
        clear_screen()
        apt("list", "--upgradable")
        print_color("Enter 'b' to go back.", "yellow")
        package_name = prompt_package("Enter the package name to upgrade: ")
        if package_name is None:
            break
        apt_get("install", "--only-upgrade", package_name)
        pause()


def autoremove() -> None:
    apt_get("autoremove")
    print_color("Apt autoremove completed.", "green")
    pause()


def autoclean_package_cache() -> None:
    apt_get("autoclean")
    print_color("Apt autoclean completed.", "green")
    pause()


def clean_package_cache() -> None:
    apt_get("clean")
    print_color("Apt cache cleaned.", "green")
    pause()


def system_information() -> None:
    commands = [
        [require_command("uname"), "-a"],
        [require_command("lsb_release"), "-a"] if find_command("lsb_release") else None,
        [require_command("lscpu")],
    ]
    for command in commands:
        if command is None:
            print_color("lsb_release is not installed; skipping distro release details.", "yellow")
            continue
        run_command(command)
    pause()


def install_package() -> None:
    package_name = prompt_package("Enter the package name to install: ")
    if package_name:
        apt_get("install", package_name)
        pause()


def remove_package() -> None:
    package_name = prompt_package("Enter the package name to remove: ")
    if package_name:
        apt_get("remove", package_name)
        pause()


def purge_package() -> None:
    package_name = prompt_package("Enter the package name to purge: ")
    if package_name:
        apt_get("purge", package_name)
        pause()


def show_package_details() -> None:
    package_name = prompt_package("Enter the package name to inspect: ")
    if package_name:
        apt("show", package_name)
        pause()


def list_installed_packages() -> None:
    apt("list", "--installed")
    pause()


def show_held_packages() -> None:
    apt_mark("showhold")
    pause()


def hold_package() -> None:
    package_name = prompt_package("Enter the package name to hold: ")
    if package_name:
        apt_mark("hold", package_name)
        pause()


def unhold_package() -> None:
    package_name = prompt_package("Enter the package name to unhold: ")
    if package_name:
        apt_mark("unhold", package_name)
        pause()


def search_packages() -> None:
    search_term = input(colorize("Enter the package name to search: ", "yellow")).strip()
    if search_term:
        apt("search", search_term)
    pause()


def list_available_upgrades() -> None:
    clear_screen()
    apt("list", "--upgradable")
    pause()


def memory_usage() -> None:
    run_command([require_command("free"), "-h"])
    pause()


def system_load() -> None:
    run_command([require_command("uptime")])
    pause()


def disk_usage_report() -> None:
    run_command([require_command("df"), "-h"])
    pause()


def network_status() -> None:
    network_command = find_command("ip")
    if network_command:
        run_command([network_command, "addr", "show"])
    elif find_command("ifconfig"):
        run_command([require_command("ifconfig")])
    else:
        print_color("Neither 'ip' nor 'ifconfig' is installed.", "red")
    pause()


def hardware_information() -> None:
    run_command([require_command("lsblk")])
    pause()


def hostname_details() -> None:
    if find_command("hostnamectl"):
        run_command([require_command("hostnamectl")])
    else:
        run_command([require_command("hostname")])
    pause()


def process_snapshot() -> None:
    run_command([require_command("ps"), "aux", "--sort=-%mem"])
    pause()


def network_routes() -> None:
    run_command([require_command("ip"), "route", "show"])
    pause()


def listening_ports() -> None:
    if find_command("ss"):
        run_command([require_command("ss"), "-tulpn"])
    elif find_command("netstat"):
        run_command([require_command("netstat"), "-tulpn"])
    else:
        print_color("Neither 'ss' nor 'netstat' is installed.", "red")
    pause()


def dns_information() -> None:
    if find_command("resolvectl"):
        run_command([require_command("resolvectl"), "status"])
    elif os.path.exists("/etc/resolv.conf"):
        run_command([require_command("cat"), "/etc/resolv.conf"])
    else:
        print_color("No resolver status tool or /etc/resolv.conf file found.", "red")
    pause()


def failed_services() -> None:
    run_command([require_command("systemctl"), "--failed"])
    pause()


def running_services() -> None:
    run_command([require_command("systemctl"), "list-units", "--type=service", "--state=running", "--no-pager"])
    pause()


def recent_error_logs() -> None:
    run_command([require_command("journalctl"), "-p", "3", "-xb", "--no-pager"])
    pause()


def poweroff_system() -> None:
    if not sys.stdin.isatty():
        print_color("Power off requires an interactive confirmation; cancelled.", "yellow")
        return
    answer = input(colorize("Power off now? [y/N]: ", "yellow")).strip().lower()
    if answer not in {"y", "yes"}:
        print_color("Power off cancelled.", "yellow")
        pause()
        return
    run_command([require_command("shutdown"), "now"])


def auto_update_system() -> None:
    success = run_sequence(
        [
            [require_command("apt-get"), "update"],
            [require_command("apt-get"), "upgrade", "-y"],
        ]
    )
    if success:
        print_color("Auto-update completed successfully.", "green")
    pause()


def reboot_system() -> None:
    if not sys.stdin.isatty():
        print_color("Reboot requires an interactive confirmation; cancelled.", "yellow")
        return
    answer = input(colorize("Reboot now? [y/N]: ", "yellow")).strip().lower()
    if answer not in {"y", "yes"}:
        print_color("Reboot cancelled.", "yellow")
        pause()
        return
    run_command([require_command("reboot")])


def exit_program() -> None:
    print_color("Exiting... Goodbye!", "red")
    sys.exit(0)


def print_banner(message: str | None = None) -> None:
    clear_screen()
    palette = ["cyan", "blue", "magenta", "blue", "cyan", "green"]
    print()
    for line, color in zip(ART_LINES, palette):
        print_color(line.center(MENU_WIDTH), color)
    print(colorize_parts([("  ━━━━━ ", "cyan"), (TAGLINE.center(MENU_WIDTH - 16), "white"), (" ━━━━━", "magenta")]))
    print()
    if message:
        print_box([f"✨ {message}"], title="Status", color="yellow")
        print()


def visible_width(text: str) -> int:
    """Return the approximate terminal display width for text."""
    width = 0
    for character in text:
        width += character_width(character)
    return width


def character_width(character: str) -> int:
    """Return the approximate terminal display width for one character."""
    if unicodedata.combining(character):
        return 0
    return 2 if unicodedata.east_asian_width(character) in {"F", "W"} else 1


def fit_text(text: str, width: int) -> str:
    """Pad or trim text to fit a fixed-width menu cell."""
    fitted = ""
    current_width = 0
    for character in text:
        next_width = current_width + character_width(character)
        if next_width > width:
            trimmed = fitted.rstrip()
            while trimmed and visible_width(f"{trimmed}…") > width:
                trimmed = trimmed[:-1]
            return f"{trimmed}…" + " " * max(0, width - visible_width(f"{trimmed}…"))
        fitted += character
        current_width = next_width
    return fitted + " " * max(0, width - current_width)


def print_box(lines: list[str], *, title: str | None = None, color: str = "cyan") -> None:
    """Print a centered box around one or more text lines."""
    indent = "  "
    top = "╭" + "─" * MENU_INNER_WIDTH + "╮"
    bottom = "╰" + "─" * MENU_INNER_WIDTH + "╯"
    if title:
        title_text = f" {title} "
        start = max(2, ((MENU_INNER_WIDTH - visible_width(title_text)) // 2) - 2)
        end = MENU_INNER_WIDTH - start - visible_width(title_text)
        top = "╭" + "─" * start + title_text + "─" * end + "╮"
    print_color(f"{indent}{top}", color)
    for line in lines:
        print_color(f"{indent}│ {fit_text(line, MENU_INNER_WIDTH - 2)} │", color)
    print_color(f"{indent}{bottom}", color)


def build_menu() -> list[MenuItem]:
    return [
        MenuItem("1", "Refresh package lists", refresh_package_lists, "Update & repair", "🔄", "Run apt-get update"),
        MenuItem("2", "Regular upgrade", regular_upgrade, "Update & repair", "⬆", "Upgrade installed packages"),
        MenuItem("3", "Distribution upgrade", distribution_upgrade, "Update & repair", "⤴", "Handle dependency changes"),
        MenuItem("4", "Full upgrade", full_upgrade, "Update & repair", "⚡", "More aggressive upgrade path"),
        MenuItem("5", "Simulate upgrade", simulate_upgrade, "Update & repair", "🧪", "Preview package changes"),
        MenuItem("6", "Fix broken packages", fix_broken_packages, "Update & repair", "🧰", "Repair dependency issues"),
        MenuItem("7", "Configure pending dpkg", configure_pending_packages, "Update & repair", "📦", "Finish installs"),
        MenuItem("8", "Auto-update system", auto_update_system, "Update & repair", "🤖", "Update and upgrade with -y"),
        MenuItem("9", "List available upgrades", list_available_upgrades, "Package lab", "☰", "Show pending updates"),
        MenuItem("10", "Upgrade specific package", upgrade_specific_package, "Package lab", "🎯", "Pick package"),
        MenuItem("11", "Install a package", install_package, "Package lab", "+", "Install something new"),
        MenuItem("12", "Remove a package", remove_package, "Package lab", "−", "Uninstall a package"),
        MenuItem("13", "Purge a package", purge_package, "Package lab", "🔥", "Remove package and configs"),
        MenuItem("14", "Search packages", search_packages, "Package lab", "⌕", "Find packages in apt"),
        MenuItem("15", "Package details", show_package_details, "Package lab", "🔎", "Show apt package info"),
        MenuItem("16", "List installed packages", list_installed_packages, "Package lab", "📚", "Show installed"),
        MenuItem("17", "Show held packages", show_held_packages, "Package lab", "🧷", "List packages on hold"),
        MenuItem("18", "Hold package", hold_package, "Package lab", "⛔", "Prevent package upgrades"),
        MenuItem("19", "Unhold package", unhold_package, "Package lab", "✅", "Allow package upgrades"),
        MenuItem("20", "Apt autoremove", autoremove, "Cleanup crew", "🧹", "Remove unused dependencies"),
        MenuItem("21", "Apt autoclean", autoclean_package_cache, "Cleanup crew", "🫧", "Drop obsolete cache files"),
        MenuItem("22", "Apt clean", clean_package_cache, "Cleanup crew", "🚿", "Clear package cache"),
        MenuItem("23", "System information", system_information, "System dashboard", "ℹ", "Kernel, release, and CPU"),
        MenuItem("24", "Hostname details", hostname_details, "System dashboard", "🏷 ", "Show host identity"),
        MenuItem("25", "Memory usage", memory_usage, "System dashboard", "▣", "Show RAM and swap usage"),
        MenuItem("26", "System load", system_load, "System dashboard", "⌁", "Display uptime and load"),
        MenuItem("27", "Disk usage report", disk_usage_report, "System dashboard", "◫", "Show filesystem usage"),
        MenuItem("28", "Hardware information", hardware_information, "System dashboard", "▤", "List block devices"),
        MenuItem("29", "Process snapshot", process_snapshot, "System dashboard", "🧠", "Sort processes by memory"),
        MenuItem("30", "Network interfaces", network_status, "Network tools", "◎", "Inspect network interfaces"),
        MenuItem("31", "Routing table", network_routes, "Network tools", "🧭", "Show IP routes"),
        MenuItem("32", "Listening ports", listening_ports, "Network tools", "📡", "Show open sockets"),
        MenuItem("33", "DNS information", dns_information, "Network tools", "🌐", "Show resolver details"),
        MenuItem("34", "Failed services", failed_services, "Logs & services", "🚨", "Show systemd failures"),
        MenuItem("35", "Running services", running_services, "Logs & services", "🟢", "List active services"),
        MenuItem("36", "Recent error logs", recent_error_logs, "Logs & services", "🧾", "Show journal errors"),
        MenuItem("37", "Reboot", reboot_system, "Power deck", "⏻", "Restart this machine"),
        MenuItem("38", "Power off", poweroff_system, "Power deck", "⏽", "Shut down this machine"),
        MenuItem("39", "Exit", exit_program, "Power deck", "×", "Close Updateme"),
    ]


def group_menu_items(menu_items: list[MenuItem]) -> dict[str, list[MenuItem]]:
    """Return menu items grouped by display category in first-seen order."""
    grouped: dict[str, list[MenuItem]] = {}
    for item in menu_items:
        grouped.setdefault(item.category, []).append(item)
    return grouped


def menu_row(item: MenuItem, width: int) -> str:
    """Format a single menu item row for a fixed-width column."""
    return fit_text(f"[{item.number:>2}] {item.icon} {item.label} — {item.description}", width)


def menu_grid_rows(items: list[MenuItem]) -> list[str]:
    """Format menu items into a wider two-column grid to reduce vertical length."""
    content_width = MENU_INNER_WIDTH - 2
    column_width = (content_width - MENU_COLUMN_GAP) // MENU_COLUMNS
    rows: list[str] = []
    left_items = items[: (len(items) + 1) // 2]
    right_items = items[(len(items) + 1) // 2 :]

    for index, left_item in enumerate(left_items):
        left_column = menu_row(left_item, column_width)
        right_column = menu_row(right_items[index], column_width) if index < len(right_items) else " " * column_width
        rows.append(f"{left_column}{' ' * MENU_COLUMN_GAP}{right_column}")
    return rows


def print_menu(menu_items: list[MenuItem]) -> None:
    dashboard_lines = [
        "Pick a number. Dangerous actions ask before they run.",
        f"{len(menu_items)} tools loaded across {len(group_menu_items(menu_items))} upgraded sections in a wider two-column layout.",
    ]
    print_box(dashboard_lines, title="🚀 COMMAND CENTER", color="magenta")
    print()

    grouped = group_menu_items(menu_items)
    for category, items in grouped.items():
        rows = menu_grid_rows(items)
        print_box(rows, title=category, color=CATEGORY_COLORS.get(category, "cyan"))
        print()


def check_environment() -> None:
    """Warn users when running outside a Debian-like apt environment."""
    if not find_command("apt-get") or not find_command("apt"):
        print_color("This tool requires apt and apt-get. It is intended for Debian-based systems.", "red")
        sys.exit(1)
    if platform.system() != "Linux":
        print_color("This tool is intended for Linux systems.", "red")
        sys.exit(1)


def run_interactive(skip_update: bool = False) -> None:
    check_environment()
    if not skip_update:
        print_banner("Gathering updates for you...")
        run_update()
        pause()

    menu_items = build_menu()
    actions = {item.number: item.action for item in menu_items}

    while True:
        print_banner()
        print_menu(menu_items)
        choice = input(colorize("  🚀 Launch option: ", "yellow")).strip()
        action = actions.get(choice)
        if action is None:
            print_color("That option is not on the menu. Please choose one of the listed numbers.", "red")
            pause()
            continue
        action()


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Interactive Debian/Ubuntu system update helper.")
    parser.add_argument(
        "--skip-initial-update",
        action="store_true",
        help="open the menu without running apt-get update first",
    )
    return parser.parse_args()


def main() -> int:
    args = parse_args()
    try:
        run_interactive(skip_update=args.skip_initial_update)
    except KeyboardInterrupt:
        print("\nExiting... Goodbye!")
        return 130
    return 0


if __name__ == "__main__":
    sys.exit(main())

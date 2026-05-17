<img width="1448" height="1086" alt="UpdatemeV2 0 May 14, 2026" src="https://github.com/user-attachments/assets/cca33fa5-756c-43e0-ac50-e3c173df4abf" />


# Updateme - by WastelandSYS

<img width="1032" height="1012" alt="updatemeV2 0" src="https://github.com/user-attachments/assets/2323e422-3a5c-4e32-a278-091d6dbe2295" />


---

## Overview

Updateme is an interactive Python helper for routine maintenance on Debian-based Linux distributions. It wraps common `apt`, system information, and housekeeping commands in a simple terminal menu.

## What changed in this polish pass

- Safer command execution with `subprocess.run([...])` instead of shell-formatted commands.
- Package names and search terms are passed as arguments, reducing accidental shell injection risk.
- Better startup checks for Linux, `apt`, and `apt-get` before showing the menu.
- Automatic `sudo` usage when needed, while still working cleanly when already running as root.
- Confirm-before-reboot behavior.
- `ip addr show` is preferred for network status, with `ifconfig` used only as a fallback.
- Optional `--skip-initial-update` flag for opening the menu immediately.
- Redesigned command center menu with grouped sections, icons, cleaner borders, and short descriptions for each action.
- Expanded from a basic updater into a 39-option maintenance cockpit with package repair, package holds, cache cleanup, network checks, service checks, and journal error views.
- Added a brighter banner, a wider two-column command center, category-specific menu colors, and interactive-only confirmations for reboot and power-off actions.
- Idempotent installer that installs Python 3, makes the script executable, and refreshes the `/usr/local/bin/updateme` symlink.

## Key features

### Update & repair

- Refresh package lists
- Regular, distribution, and full upgrades
- Simulate upgrades before applying changes
- Fix broken packages
- Configure interrupted `dpkg` installs
- Auto-update system

### Package lab

- Upgrade a specific package
- Install, remove, or purge packages
- Search packages and inspect package details
- List installed packages and available upgrades
- Show, hold, and unhold packages

### Cleanup crew

- Autoremove unused dependencies
- Autoclean obsolete cache files
- Clean the apt package cache

### System dashboard

- System information
- Hostname details
- Memory usage
- System load
- Disk usage report
- Hardware information
- Process snapshot sorted by memory usage

### Network tools

- Network interfaces
- Routing table
- Listening ports
- DNS information

### Logs, services, and power

- Failed services
- Running services
- Recent journal error logs
- Interactive-only reboot and power-off confirmations
- Exit

## Installation

```bash
git clone https://github.com/WastelandSYS/updateme.git
cd updateme
chmod +x install.sh
sudo ./install.sh
```

Open a new terminal and run:

```bash
updateme
```

## Usage

Run the interactive menu:

```bash
updateme
```

Open the menu without running `apt-get update` first:

```bash
updateme --skip-initial-update
```

Show command-line help:

```bash
updateme --help
```

## Requirements

- Debian-based Linux distribution
- Python 3
- `apt` and `apt-get`
- `sudo` when running as a non-root user

This script has been tested on an RPI 4b running Kali Linux ARM.

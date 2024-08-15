#!/usr/bin/env python3

import time
import os
import sys

# Enhanced ASCII Art Banner with Center Alignment and Color
art = """ \033[34m
                           d8b
                           88P              d8P
                          d88            d888888P
  ?88   d8P?88,.d88b, d888888   d888b8b  ?88' d8888b  88bd8b,d88b  d8888b
  d88   88 `?88'  ?88d8P' ?88  d8P' ?88  88P d8b_,dP  88P'`?8P'?8bd8b_,dP
  ?8(  d88   88b  d8P88b  ,88b 88b  ,88b 88b 88b     d88  d88  88P88b
  `?88P'?8b  888888P'`?88P'`88b`?88P'`88b`?8b`?888P'd88' d88'  88b`?888P'
             88P'
  ========  d88  ========================================================
  ========  ?8P  ========================================================
\033[0m                                                          \033[37m - TheJuicePapi\033
"""

def clear_screen():
    """
    Clears the terminal screen.
    """
    os.system('clear' if os.name == 'posix' else 'cls')

def print_color(text, color):
    """
    Prints the specified text in the specified color.
    """
    colors = {
        'black': '\033[30m',
        'red': '\033[31m',
        'green': '\033[32m',
        'yellow': '\033[33m',
        'blue': '\033[34m',
        'magenta': '\033[35m',
        'cyan': '\033[36m',
        'white': '\033[37m',
        'reset': '\033[0m'
    }
    if color in colors:
        print(colors[color] + text + colors['reset'])
    else:
        print(text)

# Initial check for updates message
clear_screen()
print(art)
print_color("                        Gathering updates for you...    ", "red")
print_color("                  ||==================================||", "red")
print("                                                                     \n")
time.sleep(1.5)  # Wait for 1.5 seconds

# Run update
os.system('sudo apt-get update')

try:
    while True:
        clear_screen()
        print(art)
        # Enhanced Menu with Color and Borders
        print_color("                  ************************************** ", "cyan")
        print_color("                  * ╔════════════════════════════════╗ * ", "cyan")
        print_color("                  * ║          \033[31mUpgrade Type\033[36m          ║ * ", "cyan")
        print_color("                  * ╠════════════════════════════════╣ * ", "cyan")
        print_color("                  * ║ 1. Regular upgrade             ║ * ", "cyan")
        print_color("                  * ║ 2. Distribution upgrade        ║ * ", "cyan")
        print_color("                  * ║ 3. Full upgrade                ║ * ", "cyan")
        print_color("                  * ║ 4. Upgrade Specific Package    ║ * ", "cyan")
        print_color("                  * ║ 5. Apt autoremove              ║ * ", "cyan")
        print_color("                  * ║ 6. Check System Information    ║ * ", "cyan")
        print_color("                  * ║ 7. Install a Package           ║ * ", "cyan")
        print_color("                  * ║ 8. Remove a Package            ║ * ", "cyan")
        print_color("                  * ║ 9. Search Packages             ║ * ", "cyan")
        print_color("                  * ║ 10. List Available Upgrades    ║ * ", "cyan")
        print_color("                  * ║ 11. Memory Usage               ║ * ", "cyan")
        print_color("                  * ║ 12. System Load                ║ * ", "cyan")
        print_color("                  * ║ 13. Disk Usage Report          ║ * ", "cyan")
        print_color("                  * ║ 14. Network Status             ║ * ", "cyan")
        print_color("                  * ║ 15. Hardware Information       ║ * ", "cyan")
        print_color("                  * ║ 16. Auto-Update System         ║ * ", "cyan")
        print_color("                  * ║ 17. Reboot                     ║ * ", "cyan")
        print_color("                  * ║ 18. Exit                       ║ * ", "cyan")
        print_color("                  * ╚════════════════════════════════╝ * ", "cyan")
        print_color("                  ************************************** ", "cyan")
        print_color("                                                          ", "cyan")

        # Handle the user's choice
        upgrade_type = input("\033[33mChoose an upgrade type: \033[0m")

        if upgrade_type == "1":
            os.system('sudo apt-get upgrade')
        elif upgrade_type == "2":
            os.system('sudo apt-get dist-upgrade')
        elif upgrade_type == "3":
            os.system('sudo apt-get full-upgrade')
        elif upgrade_type == "4":
            while True:
                clear_screen()
                os.system('sudo apt list --upgradable')
                print_color("Enter 'b' to go back.", "yellow")
                # Ask for a specific package to upgrade
                package_name = input("\033[33mEnter the package name to upgrade: \033[0m")
                if package_name.lower() == 'b':
                    break
                os.system(f'sudo apt-get install --only-upgrade {package_name}')
        elif upgrade_type == "5":
            os.system('sudo apt autoremove')
            print_color("Apt autoremove completed.", "green")
            input("\033[33mPress Enter to return to the main menu...\033[0m")
        elif upgrade_type == "6":
            os.system('uname -a && lsb_release -a && lscpu')
            input("\033[33mPress Enter to return to the main menu...\033[0m")
        elif upgrade_type == "7":
            package_name = input("\033[33mEnter the package name to install: \033[0m")
            os.system(f'sudo apt-get install {package_name}')
        elif upgrade_type == "8":
            package_name = input("\033[33mEnter the package name to remove: \033[0m")
            os.system(f'sudo apt-get remove {package_name}')
        elif upgrade_type == "9":
            # Search packages with root access
            search_term = input("\033[33mEnter the package name to search: \033[0m")
            os.system(f'sudo apt search {search_term}')
            input("\033[33mPress Enter to return to the main menu...\033[0m")
        elif upgrade_type == "10":
            # List Available Upgrades
            clear_screen()
            os.system('sudo apt list --upgradable')
            input("\033[33mPress Enter to return to the main menu...\033[0m")
        elif upgrade_type == "11":
            os.system('free -h')
            input("\033[33mPress Enter to return to the main menu...\033[0m")
        elif upgrade_type == "12":
            os.system('uptime')
            input("\033[33mPress Enter to return to the main menu...\033[0m")
        elif upgrade_type == "13":
            os.system('df -h')
            input("\033[33mPress Enter to return to the main menu...\033[0m")
        elif upgrade_type == "14":
            os.system('ifconfig')
            input("\033[33mPress Enter to return to the main menu...\033[0m")
        elif upgrade_type == "15":
            os.system('lsblk')
            input("\033[33mPress Enter to return to the main menu...\033[0m")
        elif upgrade_type == "16":
            os.system('sudo apt-get update && sudo apt-get upgrade -y')
            input("\033[33mPress Enter to return to the main menu...\033[0m")
        elif upgrade_type == "17":
            os.system('sudo reboot')
        elif upgrade_type == "18":
            print_color("Exiting... Goodbye!", "red")
            sys.exit(0)
        else:
            print_color("Invalid option. Please try again.", "red")

except KeyboardInterrupt:
    print("\nExiting... Goodbye!")
    sys.exit(0)

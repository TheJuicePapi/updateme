#!/usr/bin/env python3

art = """
                           d8b
                           88P              d8P
                          d88            d888888P
  ?88   d8P?88,.d88b, d888888   d888b8b    ?88'   d8888b  88bd8b,d88b  d8888b
  d88   88 `?88'  ?88d8P' ?88  d8P' ?88    88P   d8b_,dP  88P'`?8P'?8bd8b_,dP
  ?8(  d88   88b  d8P88b  ,88b 88b  ,88b   88b   88b     d88  d88  88P88b
  `?88P'?8b  888888P'`?88P'`88b`?88P'`88b  `?8b  `?888P'd88' d88'  88b`?888P'
             88P'
  ========  d88  ============================================================
  ========  ?8P  ============================================================
   *             *          *            *           *            *         *
 *   *       *      *  *         *    *      *          *     *      *     *
  *     *       *         *   *          *        *              *      *    *
    *      *         *            *          *        *      *       *
"""

print(art)

import time
import os
import sys
import shutil

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

# Initial check for updates
time.sleep(1)  # Wait for 1 second
print("      []          *           *          *              *             []")
print("      ||==============================================================||")
print("      ||                 Gathering updates for you...                 ||")
print("      ||==============================================================||")
print("      []                                                              []")
print("                                                                        ")
time.sleep(1.5)  # Wait for 1.5 seconds
# Run update
os.system('sudo apt-get update')

try:
    while True:
        # Extended menu with additional options
        print("                                                          ")
        print("                   ************************************** ")
        print("                   * ╔════════════════════════════════╗ * ")
        print("                   * ║          Upgrade Type          ║ * ")
        print("                   * ╠════════════════════════════════╣ * ")
        print("                   * ║ 1. Regular upgrade             ║ * ")
        print("                   * ║ 2. Distribution upgrade        ║ * ")
        print("                   * ║ 3. Full upgrade                ║ * ")
        print("                   * ║ 4. Upgrade Specific Package    ║ * ")
        print("                   * ║ 5. Apt autoremove              ║ * ")
        print("                   * ║ 6. Check System Information    ║ * ")
        print("                   * ║ 7. Disk Space Information      ║ * ")
        print("                   * ║ 8. Install a Package           ║ * ")
        print("                   * ║ 9. Remove a Package            ║ * ")
        print("                   * ║ 10. Search Packages            ║ * ")
        print("                   * ║ 11. Files                      ║ * ")
        print("                   * ║ 12. Reboot                     ║ * ")
        print("                   * ║ 13. Exit                       ║ * ")
        print("                   * ╚════════════════════════════════╝ * ")
        print("                   ************************************** ")
        print("                                                          ")

        # Handle the user's choice
        upgrade_type = input("Choose an upgrade type: ")

        if upgrade_type == "1":
            os.system('sudo apt-get upgrade')
        elif upgrade_type == "2":
            os.system('sudo apt-get dist-upgrade')
        elif upgrade_type == "3":
            os.system('sudo apt-get full-upgrade')
        elif upgrade_type == "4":
            while True:
                # List available upgrades
                os.system('sudo apt list --upgradable')
                print("Enter 'b' to go back.")
                # Ask for a specific package to upgrade
                package_name = input("Enter the package name to upgrade: ")
                if package_name.lower() == 'b':
                    break
                os.system(f'sudo apt-get install --only-upgrade {package_name}')
        elif upgrade_type == "5":
            os.system('sudo apt autoremove')
            print("Apt autoremove completed.")
            input("Press Enter to return to the main menu...")
        elif upgrade_type == "6":
            os.system('uname -a && lsb_release -a && lscpu')
            input("Press Enter to return to the main menu...")
        elif upgrade_type == "7":
            os.system('df -h')
            input("Press Enter to return to the main menu...")
        elif upgrade_type == "8":
            package_name = input("Enter the package name to install: ")
            os.system(f'sudo apt-get install {package_name}')
        elif upgrade_type == "9":
            package_name = input("Enter the package name to remove: ")
            os.system(f'sudo apt-get remove {package_name}')
        elif upgrade_type == "10":
            # Search packages with root access
            search_term = input("Enter the package name to search: ")
            os.system(f'sudo apt search {search_term}')
        elif upgrade_type == "11":
            # Files submenu
            while True:
                print("                                                          ")
                print("                   ************************************** ")
                print("                   * ╔════════════════════════════════╗ * ")
                print("                   * ║         Files Options          ║ * ")
                print("                   * ╠════════════════════════════════╣ * ")
                print("                   * ║ 1. Create a File               ║ * ")
                print("                   * ║ 2. Create a Directory          ║ * ")
                print("                   * ║ 3. Delete a File/Directory     ║ * ")
                print("                   * ║ 4. Rename a File/Directory     ║ * ")
                print("                   * ║ 5. List Files in Directory     ║ * ")
                print("                   * ║ 6. Go Back                     ║ * ")
                print("                   * ╚════════════════════════════════╝ * ")
                print("                   ************************************** ")
                print("                                                          ")
                files_option = input("Choose a files option: ")

                if files_option == "1":
                    # Create a file
                    file_name = input("Enter the name of the file: ")
                    file_path = input("Enter the path where you want to create the file: ")
                    os.system(f'touch {file_path}/{file_name}')
                    print(f"File '{file_name}' created at '{file_path}'.")
                elif files_option == "2":
                    # Create a directory
                    dir_name = input("Enter the name of the directory: ")
                    dir_path = input("Enter the path where you want to create the directory: ")
                    os.system(f'mkdir {dir_path}/{dir_name}')
                    print(f"Directory '{dir_name}' created at '{dir_path}'.")
                elif files_option == "3":
                    # Delete a file/directory
                    file_dir_path = input("Enter the path of the file/directory to delete: ")
                    os.system(f'rm -r {file_dir_path}')
                    print(f"File/Directory at '{file_dir_path}' deleted.")
                elif files_option == "4":
                    # Rename a file/directory
                    old_name = input("Enter the current name of the file/directory: ")
                    new_name = input("Enter the new name for the file/directory: ")
                    os.system(f'mv {old_name} {new_name}')
                    print(f"File/Directory '{old_name}' renamed to '{new_name}'.")
                elif files_option == "5":
                    # List files in directory
                    dir_path = input("Enter the path of the directory to list files: ")
                    os.system(f'ls {dir_path}')
                elif files_option == "6":
                    # Go back to main menu
                    break
                else:
                    print("Invalid input. Please enter a valid option.")
        elif upgrade_type == "12":
            os.system('sudo reboot')
        elif upgrade_type == "13":
            raise KeyboardInterrupt
        else:
            print("Invalid input.")
except KeyboardInterrupt:
    # Handle Ctrl+C interruption
    print("\n                                             ")
    print_color("                            ( EXITING SCRIPT )", "red")
    time.sleep(1)  # Wait for 1 second
    art = """
  +========================================================================+
  ||  _____ _              _          __                   _           _  ||
  || |_   _| |_  __ _ _ _ | |__ ___  / _|___ _ _   _  _ __(_)_ _  __ _| | ||
  ||   | | | ' \/ _` | ' \| / /(_-< |  _/ _ \ '_| | || (_-< | ' \/ _` |_| ||
  ||   |_| |_||_\__,_|_||_|_\_\/__/ |_| \___/_|    \_,_/__/_|_||_\__, (_) ||
  ||                                                              |___/   ||
  +========================================================================+
    """
    print(art)
    sys.exit()

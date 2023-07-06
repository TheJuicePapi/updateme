#!/usr/bin/python3

import time
import os
import sys
import shutil

from subprocess import run
from pathlib import Path


class UpdateMe:
    def __init__(self):
        print(self.displayArt("start"))
        self.createShortcut()
        self.update()

    def displayArt(self, art):
        """
        Call this method, to display art.
        """
        start = """
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
   *    *      *      *  *         *    *      *          *     *      *    *    *
     *    *       *         *   *          *       *               *     *    *
   *    *      *       *             *         *        *      *       *    *    *
           *                  *                    *               *
        """

        thank_you = """

       +========================================================================+
       ||  _____ _              _          __                   _           _  ||
       || |_   _| |_  __ _ _ _ | |__ ___  / _|___ _ _   _  _ __(_)_ _  __ _| | ||
       ||   | | | ' \/ _` | ' \| / /(_-< |  _/ _ \ '_| | || (_-< | ' \/ _` |_| ||
       ||   |_| |_||_\__,_|_||_|_\_\/__/ |_| \___/_|    \_,_/__/_|_||_\__, (_) ||
       ||                                                              |___/   ||
       +========================================================================+

        """
        wait = """

         []                                                               []
         ||===============================================================||
         ||                  Gathering updates for you...                 ||
         ||===============================================================||
         []                                                               []
  
        """
        prompt = """

                        **************************************
                        * ╔════════════════════════════════╗ *
                        * ║          Upgrade Type          ║ *
                        * ╠════════════════════════════════╣ *
                        * ║ 1. Regular upgrade             ║ *
                        * ║ 2. Distribution upgrade        ║ *
                        * ║ 3. Full upgrade                ║ *
                        * ║ 4. Apt autoremove              ║ *
                        * ║ 5. Exit                        ║ *
                        * ╚════════════════════════════════╝ *
                        **************************************
       
         """
        reboot = """


                        * ╔════════════════════════════════╗ *
                      *** ║   Do you want to reboot the    ║ ***
                     **** ║            system?             ║ ****
                     **** ╟────────────────────────────────╢ ****
                      *** ║        (y: YES, n: NO)         ║ ***
                        * ║================================║ *


        """
        if art == "start":
            return start
        elif art == "thank_you":
            return thank_you
        elif art == "wait":
            return wait
        elif art == "prompt":
            return prompt
        elif art == "reboot":
            return reboot

    def print_color(self, text, color):
        """
        Prints the specified text in the specified color.
        """
        colors = {
            "black": "\033[30m",
            "red": "\033[31m",
            "green": "\033[32m",
            "yellow": "\033[33m",
            "blue": "\033[34m",
            "magenta": "\033[35m",
            "cyan": "\033[36m",
            "white": "\033[37m",
            "reset": "\033[0m",
        }
        return f'{colors[color]}{text}{colors["reset"]}' if color in colors else text

    def update(self):
        """
        Run update at start of program.
        """
        time.sleep(1)  # Wait for 1 seconds
        print(self.displayArt("wait"))
        time.sleep(1.5)  # Wait for 1.5 seconds

        # Run update
        os.system("sudo apt-get update")

    def exitScript(self, message):
        time.sleep(0.5)  # Wait for .5 seconds
        # Exit script
        print(self.print_color("\n                                  ( EXITING SCRIPT )", "red"))
        time.sleep(1)  # Wait for 1 seconds
        print(self.displayArt(message))
        sys.exit()

    def createShortcut(self):
        """
        creates a hard symbolic link in usr/bin.
        """
        file_name = Path(__file__).resolve()
        create_link = 'n' if file_name.name == "updateme" else input("                Do you want to create a shortcut for updateme? [y/n]")

        commands = [
            f"sudo cp -l {file_name} updateme",
            "sudo chmod +x updateme",
            "sudo mv updateme /usr/bin/updateme"
        ]

        if "y" in create_link:
            if Path("/usr/bin/updateme").exists():
                run("sudo rm /usr/bin/updateme".split())  # [WARNING]: DO NOT MODIFY THIS COMMAND (-f)
            for command in commands:
                run(command.split())
            print("Added to terminal use command: <updatme>")

    def promptCommands(self):
        """
        Main program: Show prompts.
        """
        print(self.displayArt("prompt"))
        # self.createShortcut()

        upgrade_commands = [
            "sudo apt upgrade -y",  # 0
            "sudo apt dist-upgrade -y",  # 1
            "sudo apt full-upgrade -y",  # 2
            "sudo apt autoremove",  # 3
        ]
        while True:
            try:
                UPGRADE_TYPE = int(input("                               Choose an upgrade type: ")) - 1

                if UPGRADE_TYPE == 4:
                    self.exitScript("thank_you")
                else:
                    os.system(upgrade_commands[UPGRADE_TYPE])
            except ValueError:
                print("Invalid input ~[1-5]")
                continue
            except IndexError:
                print("Invalid input ~[1-5]")
                continue
            except KeyboardInterrupt:
                self.exitScript("thank_you")
            else:
                self.rebootSys()
        # self.rebootSys()

    def rebootSys(self):
        """
        Call this to ask for Reboot.
        """
        while True:
            reboot_choice = input(self.displayArt("reboot") + "\n                               Please choose an option:")

            if "y" in reboot_choice:
                # Reboot the system
                os.system("sudo reboot")
            elif "n" in reboot_choice:
                self.exitScript("thank_you")
            else:
                print("Invalid input.")
                continue


if __name__ == "__main__":
    upd = UpdateMe()
    upd.promptCommands()


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

time.sleep(1) # Wait for 1 seconds
print("     []          *           *          *              *             []")
print("     ||==============================================================||")
print("     ||                 Gathering updates for you...                 ||")
print("     ||==============================================================||")
print("     []                                                              []")
print("                                                                       ")
time.sleep(1.5) # Wait for 1.5 seconds


# Run update
os.system('sudo apt-get update')


# Prompt update options
print("                                                        ")
print("                 ************************************** ")
print("                 * ╔════════════════════════════════╗ * ")
print("                 * ║           Upgrade Type         ║ * ")
print("                 * ╠════════════════════════════════╣ * ")
print("                 * ║ 1. Regular upgrade             ║ * ")
print("                 * ║ 2. Distribution upgrade        ║ * ")
print("                 * ║ 3. Apt autoremove              ║ * ")
print("                 * ║ 4. Exit                        ║ * ")
print("                 * ╚════════════════════════════════╝ * ")
print("                 ************************************** ")
print("                                                        ")
upgrade_type = input("Choose an upgrade type: ")

if upgrade_type == "1":
   # Run upgrade to install package updates
  os.system('sudo apt-get upgrade')
elif upgrade_type == "2":
   # Run dist upgrade to install distribution packages
  os.system('sudo apt-get dist-upgrade')
elif upgrade_type == "3":
   # Run autoremove unused packages packages
  os.system('sudo apt autoremove')
elif upgrade_type == "4":
  time.sleep(.5) # Wait for .5 seconds
 # Exit script
  print("                                             ")
  print("                           ( EXITING SCRIPT )")
  time.sleep(1) # Wait for 1 seconds
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
else:
  print("Invalid input.")

# Prompt for reboot
reboot_choice = input(
"                                                        \n"
"                  * ╔════════════════════════════════╗ *\n"
"                *** ║   Do you want to reboot the    ║ ***\n"
"               **** ║            system?             ║ ****\n"
"               **** ╟────────────────────────────────╢ ****\n"
"                *** ║        (y: YES, n: NO)         ║ ***\n"
"                  * ║================================║ *\n"

)
print("Please chose an option")
if reboot_choice == "y":
  # Reboot the system
  os.system('sudo reboot')
elif reboot_choice == "n":
  time.sleep(.5) # Wait for .5 seconds
# Exit the script
  print("                                              ")
  print("                            ( EXITING SCRIPT )")
  time.sleep(1) # Wait for 1 seconds
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
else:
  print("Invalid input.")

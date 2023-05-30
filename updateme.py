                    ### A script for updating the system  ###

art = """

   __  __          __      __       __  ___
  / / / /___  ____/ /___ _/ /____  /  |/  /__
 / / / / __ \/ __  / __ `/ __/ _ \/ /|_/ / _ }
/ /_/ / /_/ / /_/ / /_/ / /_/  __/ /  / /  __/
\____/ .___/\__,_/\__,_/\__/\___/_/  /_/\___/
    /_/

"""

print(art)

import os
import sys

# Run update
os.system('sudo apt-get update')

# Prompt update options
upgrade_type = input("Choose upgrade type:\n1. Regular upgrade\n2. Distribution upgrade\n3. Exit\n")

if upgrade_type == "1":
   # Run upgrade to install package updates
  os.system('sudo apt-get upgrade')
elif upgrade_type == "2":
   # Run dist upgrade to install distribution packages
  os.system('sudo apt-get dist-upgrade')
elif upgrade_type == "3":
  # Exit script
  print("Exiting script...")
  art = """

   _____ _              _          __                   _           _
  |_   _| |_  __ _ _ _ | |__ ___  / _|___ _ _   _  _ __(_)_ _  __ _| |
    | | | ' \/ _` | ' \| / /(_-< |  _/ _ \ '_| | || (_-< | ' \/ _` |_|
    |_| |_||_\__,_|_||_|_\_\/__/ |_| \___/_|    \_,_/__/_|_||_\__, (_)
                                                              |___/
  """
  print(art)


  sys.exit()
else:
  print("Invalid input.")


# Prompt for reboot
reboot_choice = input("Do you want to reboot the system? (1: yes, 2: no)\n")

if reboot_choice == "1":
  # Reboot the system
  os.system('sudo reboot')
elif reboot_choice == "2":
  # Exit the script
  print("Exiting script...")
  art = """

   _____ _              _          __                   _           _
  |_   _| |_  __ _ _ _ | |__ ___  / _|___ _ _   _  _ __(_)_ _  __ _| |
    | | | ' \/ _` | ' \| / /(_-< |  _/ _ \ '_| | || (_-< | ' \/ _` |_|
    |_| |_||_\__,_|_||_|_\_\/__/ |_| \___/_|    \_,_/__/_|_||_\__, (_)
                                                              |___/
  """
  print(art)


  sys.exit()
else:
  print("Invalid input.")


















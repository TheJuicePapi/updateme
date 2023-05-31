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


import time 

time.sleep(1) # Wait for 1 seconds

print("Gathering updates for you...")

time.sleep(1.5) # Wait for 1.5 seconds


import os
import sys

print("=============================================================")

# Run update
os.system('sudo apt-get update')

print("=============================================================")

# Prompt update options
upgrade_type = input("Choose upgrade type:\n1. Regular upgrade\n2. Distribution upgrade\n3. Apt autoremove\n4. Exit\n")

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
  print("Exiting script...")
  time.sleep(1) # Wait for 1 seconds
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

print("=============================================================")
# Prompt for reboot
reboot_choice = input("Do you want to reboot the system? (y: yes, n: no)\n")

if reboot_choice == "y":
  # Reboot the system
  os.system('sudo reboot')
elif reboot_choice == "n":
  time.sleep(.5) # Wait for .5 seconds
# Exit the script
  print("Exiting script...")
  time.sleep(1) # Wait for 1 seconds
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


















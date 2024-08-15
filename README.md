-------------------------------------------------------------------------------------------------------------------------------------------

 Updateme - by TheJuicePapi

-------------------------------------------------------------------------------------------------------------------------------------------

![Screenshot_2024-08-14_23-14-49](https://github.com/user-attachments/assets/bea28a0d-8dd6-4745-8a25-f39ae75d48a8)
![Screenshot_2024-08-14_23-25-46](https://github.com/user-attachments/assets/68f7d9cc-ae44-4786-9be1-2a4c54919f36)
![Screenshot_2024-08-14_23-28-14](https://github.com/user-attachments/assets/8c03906e-e453-4cb4-a39f-042233a1ec8c)

------------------------------------------------------------------------------------------------------------------------------------------

Overview


Updateme is a Python script designed to streamline system updates and maintenance tasks on Debian-based Linux distributions. It provides a comprehensive menu for managing upgrades, installing and removing packages, and checking system information.

------------------------------------------------------------

Key Features


  *  Regular Upgrade: Perform a standard upgrade of installed packages.
  *  Distribution Upgrade: Upgrade the entire distribution.
  *  Full Upgrade: Perform a full upgrade of the system, including handling dependencies.
  *  Upgrade Specific Package: Upgrade a specific package.
  *  Autoremove: Remove unnecessary packages.
  *  Check System Information: Display system information including kernel version and CPU details.
  *  Install a Package: Install a new package.
  *  Remove a Package: Remove an existing package.
  *  Search Packages: Search for packages in the repository.
  *  List Available Upgrades: List packages with available updates.
  *  Memory Usage: Display memory usage statistics.
  *  System Load: Show system load statistics.
  *  Disk Usage Report: Report on disk usage.
  *  Network Status: Display network interface status.
  *  Hardware Information: Show hardware information.
  *  Auto-Update System: Perform an automatic update of the system.
  *  Reboot: Reboot the system.
  *  Exit: Exit the script.


-------------------------------

INSTALLATION & USAGE


Git clone installation:

1. 'git clone https://github.com/TheJuicePapi/updateme.git'
2. 'cd updateme'
3. 'sudo chmod +x install.sh updateme.py'
4. 'sudo ./install.sh'
5. Exit and open a new terminal to use 'updateme' shortcut

 
-------------------------------

Dependencies


For this script to work, you will need Python 3 and apt package manager. The install.sh script should automatically handle these dependencies. If needed, manually install them using:

    sudo apt-get install -y python3
    
------------------------------

This script has been tested on an RPI 4b running a kali linux arm.

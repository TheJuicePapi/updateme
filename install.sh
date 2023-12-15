#!/bin/bash

# Check if running as root
if [ "$EUID" -ne 0 ]; then
    echo "Please run as root"
    exit
fi

# Install required packages (adjust based on your needs)
apt-get update
apt-get upgrade -y

# Install Python dependencies
# No dependencies needed

# Create symbolic link for updateme.py
ln -s "$(pwd)/updateme.py" /usr/local/bin/updateme

clear

echo "Installation complete and shortcut created! You can now run updateme.py from any directory by simply typing 'updateme'."

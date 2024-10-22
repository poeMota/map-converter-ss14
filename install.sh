#!/bin/usr/env bash
if ! command -v python3 &> /dev/null; then
    echo "ERROR: Python not installed"
    exit 1
fi

if ! command -v pacman &> /dev/null; then
   if ! command -v pip3 &> /dev/null; then
       echo "ERROR: pip not installed"
       exit 1
   fi

   pip install -r requirements.txt
else
   if ! command -v yay &> /dev/null; then
       echo "ERROR: you are using Arch or Arch based Linux, you need to install yay to continue"
       exit 1
   fi

   sudo pacman -S --noconfirm python-pillow
   sudo pacman -S --noconfirm tk
   yay --noconfirm -S python-customtkinter
fi

echo "Installation completed successfully, to run the program run python main.py"


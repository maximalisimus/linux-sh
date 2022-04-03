#!/bin/bash

# clear the screen
tput clear

# Move cursor to screen location X,Y (top left is 0,0)
tput cup 3 15

# Set a foreground colour using ANSI escape
tput setaf 3
echo "XYX Corp LTD."
tput sgr0

tput cup 5 17
tput bold
# Set reverse video mode
tput rev
echo "M A I N - M E N U"
tput sgr0

tput cup 7 15
echo "1. User Management"
tput sgr0

tput cup 8 15
echo "2. Service Management"

tput cup 9 15
echo "3. Process Management"

tput cup 10 15
echo "4. Backup"

tput cup 11 15
echo "5. Exit"

# Set bold mode
tput cup 13 15
read -p "Enter your choice [1-9] " choice

tput clear
tput sgr0
tput rc


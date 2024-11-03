#!/bin/bash

# (c) 2024 KDUser12
# Licensed under the MIT License

parent_process=$(ps -o comm= -p $PPID)
file=$1

if [[ "$parent_process" == "python" || "$parent_process" == "python3" ]]; then
    # Define red color using ANSI escape codes
    RED='\033[0;31m'
    NC='\033[0m' # No Color

    # Message to display (multiple lines)
    message="Warning, you have just left PIP-Installer
to launch an independent program created and
certified by YourLabXYZ."

    # Find the longest line to determine the width of the box
    longest_line=$(echo "$message" | awk '{ if ( length > L ) { L=length } } END { print L }')

    # Create the top and bottom border based on the length of the longest line
    border=$(printf '%*s' "$longest_line" | tr ' ' '-')

    # Display the message with a red border
    echo -e "${RED}"
    echo -e "+-${border}-+"

    # Loop through each line of the message
    while IFS= read -r line; do
        printf "| %-*s |\n" "$longest_line" "$line"
    done <<< "$message"

    echo -e "+-${border}-+"
    echo -e "${NC}"

    echo "There are missing dependencies necessary to start the program."
    echo "These dependencies cannot be automatically installed by the base installer."

    read -p "Do you want to install the missing dependencies? (yes/no): " response

    if [[ "$response" == "yes" ]]; then
        if [[ -f "$file" ]]; then
            echo "Reading dependencies from $file..."

            install=false
            while IFS= read -r line; do
                if [[ "$line" == *"# Package required (not automatically installed)"* ]]; then
                    install=true
                elif [[ "$line" == *"# Package required (automatically installed)"* ]]; then
                    install=false
                fi

                if [[ "$install" == true && ! "$line" =~ ^# ]]; then
                    echo "Installing dependency: $line"
                    pip install "$line"
                fi
            done < "$file"

            echo "Restarting Python program..."
            exit 0
        else
            echo "$file not found."
            exit 1
        fi
    else
        echo "Dependency installation canceled. Exiting the program."
        exit 0
    fi
else
    echo "Error: this script must be run by a Python script."
    exit 1
fi

#!/bin/bash

# (c) 2024 KDUser12
# Licensed under the MIT License

# Checks if Python (python3 or python) is already installed
if ! command -v python3 &>/dev/null && ! command -v python &>/dev/null; then
    echo "Python is not installed. Detecting the operating system to proceed with installation..."

    # Detects the operating system
    case "$OSTYPE" in
        linux-gnu*)
            # Linux system: Check for available package manager
            if command -v apt &>/dev/null; then
                echo "Detected distribution: Debian/Ubuntu"
                sudo apt update
                sudo apt install -y python3
            elif command -v dnf &>/dev/null; then
                echo "Detected distribution: Fedora"
                sudo dnf install -y python3
            elif command -v yum &>/dev/null; then
                echo "Detected distribution: CentOS/RHEL"
                sudo yum install -y python3
            elif command -v zypper &>/dev/null; then
                echo "Detected distribution: openSUSE"
                sudo zypper install -y python3
            elif command -v pacman &>/dev/null; then
                echo "Detected distribution: Arch Linux"
                sudo pacman -Sy python --noconfirm
            else
                echo "Unsupported package manager. Manual installation required."
            fi
            ;;

        darwin*)
            # macOS system: use Homebrew if available
            echo "Detected operating system: macOS"
            if command -v brew &>/dev/null; then
                brew install python
            else
                echo "Homebrew is not installed. Please install it from https://brew.sh/"
            fi
            ;;

        msys* | cygwin*)
            # Windows system (MSYS or Cygwin)
            echo "Detected operating system: Windows"
            if command -v winget &>/dev/null; then
                echo "Installing Python with winget..."
                winget install --id Python.Python.3 -e --source winget
            else
                echo "Winget is not available. Please download and install Python from https://www.python.org/downloads/windows/"
            fi
            ;;

        *)
            # Unsupported operating system
            echo "Unsupported operating system. Manual installation of Python required."
            ;;
    esac
else
    echo "Python is already installed."
fi

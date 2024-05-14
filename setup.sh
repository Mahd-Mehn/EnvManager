#!/bin/bash

# Function to check if a Python package is installed
function check_python_package {
    PACKAGE=$1
    if ! pip show $PACKAGE &>/dev/null; then
        echo "Package $PACKAGE not found. Installing..."
        pip install $PACKAGE
    else
        echo "Package $PACKAGE is already installed."
    fi
}

# Install required Python packages
echo "Checking required Python packages..."
check_python_package pycryptodome
check_python_package gitpython

# Make the main.py script executable
echo "Making main.py executable..."
chmod +x main.py

# Add to PATH or create a symlink
TARGET_DIR="$HOME/.local/bin"
SCRIPT_NAME="envmanager"
SCRIPT_PATH="$(pwd)/main.py"

# Ensure the target directory exists
mkdir -p "$TARGET_DIR"

# Check if $TARGET_DIR is in PATH
echo "Checking if $TARGET_DIR is in PATH..."
if [[ ":$PATH:" != *":$TARGET_DIR:"* ]]; then
    echo "$TARGET_DIR is not in PATH. Adding it to PATH..."
    echo "export PATH=\$PATH:$TARGET_DIR" >> ~/.bashrc
    source ~/.bashrc
fi

# Remove existing symlink or file if it exists
if [ -f "$TARGET_DIR/$SCRIPT_NAME" ]; then
    echo "Removing existing symlink or file at $TARGET_DIR/$SCRIPT_NAME"
    rm "$TARGET_DIR/$SCRIPT_NAME"
fi

# Create a symlink to cli_tool.py in $TARGET_DIR
echo "Creating a symlink to cli_tool.py in $TARGET_DIR..."
ln -s "$SCRIPT_PATH" "$TARGET_DIR/$SCRIPT_NAME"

echo "Setup complete. You can now use 'envmanager' command."

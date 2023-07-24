#!/bin/bash

# Set the path where you want to install Miniconda
MYPATH="/goinfre/$USER/miniconda3"

# Check if Miniconda is already installed
if [ -d "$MYPATH" ]; then
    echo "Miniconda is already installed at $MYPATH."
else
    # Download the installer
    curl -LO "https://repo.anaconda.com/miniconda/Miniconda3-latest-Linux-x86_64.sh"

    # Install Miniconda
    bash Miniconda3-latest-Linux-x86_64.sh -b -p $MYPATH

    # Initialize conda with your shell
    $MYPATH/bin/conda init zsh
fi

# Set conda to not activate the base environment by default
$MYPATH/bin/conda config --set auto_activate_base false

# Source the .zshrc to make changes take effect
source '~/.zshrc'

# Create a new conda environment with the required packages
conda create --name 42AI-$USER python=3.7 jupyter pandas pycodestyle numpy

# Display information about current environments
conda info --envs

# Activate the new environment
conda activate 42AI-$USER

# Check which python is being used
which python

# Display python version
python -V

# Test python with a simple script
python -c "print('Hello World!')"


#!/bin/bash

echo "List of installed packages and their versions:"
conda list

echo "Metadata for numpy:"
conda search numpy --info

echo "Removing numpy:"
conda remove numpy -y

echo "Reinstalling numpy:"
conda install numpy -y

echo "Freezing installed packages to requirements.txt:"
pip freeze > requirements.txt
cat requirements.txt

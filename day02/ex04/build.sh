#!/bin/bash

# Upgrade pip
pip install --upgrade pip
pip install wheel

# Build the distribution packages
python setup.py sdist bdist_wheel

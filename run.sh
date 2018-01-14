#!/usr/bin/env bash
clear
sudo apt-get install python-pygame
SCRIPT_DIR="$( cd "$( dirname "$0" )" && pwd )"
cd "$SCRIPT_DIR"
python tanks.py

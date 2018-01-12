#!/usr/bin/env bash
sudo apt-get install python-pygame
SCRIPT_DIR="$( cd "$( dirname "$0" )" && pwd )"
cd "$SCRIPT_DIR"
python tanks.py

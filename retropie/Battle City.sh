#!/usr/bin/env bash
# "/opt/retropie/supplementary/runcommand/runcommand.sh" 0 _PORT_ "battle-city" "/home/pi/RetroPie/roms/ports/battle-city/tanks.py"
SCRIPT_DIR="$( cd "$( dirname "$0" )" && pwd )"
cd "$SCRIPT_DIR"
python ./source/tanks.py
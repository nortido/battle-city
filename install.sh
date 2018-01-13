#!/usr/bin/env bash
# download the file
echo "Download game..."
wget --no-check-certificate https://github.com/Nortido/battle-city/archive/master.zip
# curl -LOk https://github.com/Nortido/battle-city/archive/master.zip
# unzip the file so that we can use the things inside of it
echo "Unzip and move files..."
unzip master.zip -d /home/pi/RetroPie/roms/ports/battle-city
#move the files from the zip to the proper location
mv "/home/pi/RetroPie/roms/ports/battle-city/battle-city-master/retropie/Battle City.sh" /home/pi/RetroPie/roms/ports
mv /home/pi/RetroPie/roms/ports/battle-city/battle-city-master*/* /home/pi/RetroPie/roms/ports/battle-city
rmdir /home/pi/RetroPie/roms/ports/battle-city/battle-city-master*
rm /home/pi/RetroPie/roms/ports/master.zip
# install pygame framework
echo "Install pygame framework..."
sudo apt-get install python-pygame
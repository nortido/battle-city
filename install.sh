#!/usr/bin/env bash
# download the file
sudo wget https://github.com/Nortido/battle-city/archive/master.zip
# unzip the file so that we can use the things inside of it
sudo unzip master.zip -d /home/pi/RetroPie/roms/ports/battle-city
#move the files from the zip to the proper location
sudo mv /home/pi/RetroPie/roms/ports/battle-city/battle-city-master*/* /home/pi/RetroPie/roms/ports/battle-city
sudo rmdir /home/pi/RetroPie/roms/ports/battle-city/battle-city-master*
# install pygame framework
sudo apt-get install python-pygame
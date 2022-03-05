#!/bin/bash

RED='\033[1;31m'
NC='\033[0m'

printf "${RED}LINUX INSTALL SCRIPT${NC}\n"

printf "[*] installing requirements"

cd $HOME
sudo su
apt-get update
apt-get upgrade
apt-get install git
apt-get install python3
apt-get install pip
pip install --upgrade pip
pip install -r requirements.txt
chmod +x main.py
printf "[*] installing terminal picture viewer"
git clone https://github.com/stefanhaustein/TerminalImageViewer
sudo apt install imagemagick || yum install ImageMagick
cd TerminalImageViewer/src/main/cpp
make
make intall
cd /

sleep 2

printf "${RED}[*] Installation completed (or requirements already satisfied)${NC}\n"
echo 'Do you want to run the program? y/n'
read launch
if [ $launch == "y" ]
then
echo '[*] Running...'
python3 main.py
elif [ $launch ==  "n" ]
then
echo '[!] Exit....'
sleep 2
exit
else
echo '[!] Check your syntax, wrong input! (Case sensitive "y" or "n")'
sleep 1
echo '[!] QUITTING!'
sleep 2
exit
fi


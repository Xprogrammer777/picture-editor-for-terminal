#!/bin/bash

RED='\033[1;31m'
NC='\033[0m'

printf "${RED}LINUX INSTALL SCRIPT${NC}\n"

printf "[*] installing requirements\n"

cd $HOME
apt-get update
apt-get upgrade --fix-missing
apt-get install git
apt-get install cowsay
apt-get install bb
apt-get install python3
cd picture-editor-for-terminal
apt-get install pip
pip install --upgrade pip
pip install -r requirements.txt
chmod +x main.py
cd $HOME
printf "[*] installing terminal picture viewer\n"
git clone https://github.com/stefanhaustein/TerminalImageViewer
sudo apt install imagemagick || yum install ImageMagick
cd TerminalImageViewer/src/main/cpp
make
make intall
printf "[*] Requirements installed..."
cd picture-editor-for-terminal

sleep 2

printf "${RED}[*] Installation completed (or requirements already satisfied)${NC}\n"
echo 'Do you want to run the program? y/n \n'
read launch
if [ $launch == "y" ]
then
cowsay 'Running process started'
sleep 1
echo '[*] Running...\n'
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


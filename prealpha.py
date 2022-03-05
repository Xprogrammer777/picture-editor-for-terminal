#The script main.py have all options but a LLLLOOOOOTTT of bugs, many problem, so this is a working one, you will have no error but not all options
import time
import os
import sys
import socket
import pyfiglet
from PIL import Image, ImageFont, ImageDraw 

time.sleep(1)
print("=)")
time.sleep(1)
os.system("clear")

hostname = socket.gethostname()
banner = pyfiglet.figlet_format("PICTURE EDITOR")

#print the "welcome page" start
print(banner)
print("""
 ___________
|    / \ ¤ |
| /\/   \__|
|/_________|
""")

print("Welcome to linux picture editor ", hostname, " type 'help' for info")
#print the welcome page end

def help():
    print("""
     upscale: increase picture quality
     bg: switch in black/white
     reize: reize picture
     text : add text on your picture
     x : comming soon
    """)


def text():
    print("?")
    #TODO: Maybe I should see if we can import stuff to do this because it will be pretty hard

while True:
    cmd = input(hostname+"@piceditor -> ").lower()

    if "help" in cmd:
         help()

    elif "clear" in cmd:
         os.system("clear")

    elif "upscale" in cmd:
        print("upscale process start")

    elif "bg" in cmd:
        print("black white process start") #call the function in the other file

    elif "exit" in cmd:
        quit()
    elif cmd == "exit":
        print("Add requests on Github...")
        time.sleep(1)
        print("") 
    elif "reize" in cmd:
        print("reize proces start")

    elif "text" in cmd:
        text()
    elif cmd == "ls":
     os.system("ls")
    elif cmd == "" or cmd == " " :
        print("please, type something.")
      
    else:
        print("wrong input")
        time.sleep(1)
        os.system("clear")
        time.sleep(1)
        print(banner)


        #REPORT ANY ISSUE ON GITHUB


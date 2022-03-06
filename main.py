import time
import os
import sys
import socket
import pyfiglet
import cv2
from cv2 import dnn_superres
from PIL import Image, ImageFont, ImageDraw 
import pyperclip


#simple joke when the programm start
time.sleep(1)
print("=)")
time.sleep(1)
os.system("clear")

#get the hostname will be used as username
hostname = socket.gethostname()
#banner
banner = pyfiglet.figlet_format("PICTURE EDITOR")

#print the "welcome page" start
print(banner)
print("""
 ___________
|    / \ ☼ |
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


#upscale function start
def upscale():
    pyfiglet.format("upscale")
    sr = dnn_superres.DnnSuperResImpl_create()
    #Asking user for some basics infos : path of the picture, output path, upscale factor 
    print("image upscalling process")
    path = str(input("put the path of the picture : ")) 
    image = cv2.imread(path)  
    Image.open(path)
    width, height = Image.size #not usefull, maybe for other things but not in upscale function
    
    #time estimation code start
    if width >= 400 and  height >= 400: #if img is big so time is longer to process
        big = True
    else:
        big = False

    if big:
        print("you picture already have a good resolution, it will take some time to upscale")
        estimation = 60 #int because we will be able to change the value
    else:
        print("Ineed, we need to upscale your picture, it's very small")
        estimation = 30 #estimation is about time
    #time estimation code end

    modelressource = "/model/" #not usefull, inistialise var
    picture_name_output = str(input("Set the path/name of the output picture"))
    upscalling_ = int(input("how much you want to upscale caution don't enter crazy number or your GPU will die (2-8)"))
    #use x2 algo if higher use algo 4 if higher retake the img re-use it upscale etc....

    if upscalling_ == 2: #if upscalling = 2 so use the x2 algorithm
        modelressource == "/ressources/x2.pb"
        sr.readModel(modelressource)
        sr.setModel("edsr", 2)
        print("process started")
        print("time estimation : ", estimation, "s")
        output = sr.upsample(image)
        cv2.imwrite(picture_name_output, result)
        see = str(input("do you want to see the result y/n"))
        
        #If the user want to see the picture
        if see == "y":
            Image.show(picture_name_output)

        elif see == "n":
            print("OK")
            os.system("clear")
            print(banner)

        else:
            print("wrong input, quitting")
            quit()
    #if upscalling factor = 4 use x4 upscalling algorithm
    elif upscalling_ == 4:
        modelressource == "/model/2x.rb" # will change later
        sr.readModel(modelressource)
        sr.setModel("edsr", 4)
        print("process started")
        print("time estimation : ", estimation)
        output = sr.upsample(image)
        cv2.imwrite(picture_name_output, result)
        see = str(input("do you want to see the result y/n"))

        if see == "y":
            Image.show(picture_name_output)

        elif see == "n":
            print("OK")
            os.system("clear")
            print(banner)
        
        else:
            print("wrong input, quitting")
            quit()
    #(Little hard) : if it's > 4 we search for a multiplier of this value (by 2) and finally discrease picture quality if its not a even number
    elif upscalling_ > 4:
        print("[!] actually coding this pretty hard part check for next update")
        """
        os.system("mkdir 'temp'")
        os.system("cp image /temp/")
        
        higherforupscall = upscalling_ // 2 #know how many 2 we can put in the user's input if it's this algo
        modelressource == "/model/stuff_.rb" # will change later
    
        for calc in higherforupscall:
            print("process started")
            print("time estimation : ", estimation)
            output = sr.upsample(image)
            image = picture_name_output
            cv2.imwrite(picture_name_output, result) #maybe result will be output will see later

            #break

    
#upscale function end
"""

def bg():
    pyfiglet.format("Black white switcher")
    path = str(input("set the path of the picture"))
    picture_name_output = str(input("set the output path of your picture : "))
    Image.open(path)
    imgGray = color.rgb2gray(path)
    Image.save(picture_name_output)


def reize():

    pyfiglet.format("reize")

    path = str(input("set the path of the img you want to reize : "))
    Image.open(path)
    print("reading your picture")
    output_path = str(input("set the output path with the picture name e.g : home/username/Desktop/life.png"))
    width, heigh = Image.size
    x_reize = str(input("set the x pixels you want to reize :"))
    print("ok")
    y_reize = str(input("set the y pixel you want to reize"))
    Image.resize((x_reize, y_reize))
    path.save(output_path)
    see = str(input("do you want to see the picture?"))

    if see == "y" or see =="Y":
        Image.show(output_path)
        os.system("clear")
        time.sleep(1)
        print(banner)


def text():
    width, heigh = Image.size
    center = heigh//2, width//2
    bottom = heigh//2, width//4
    # Set differents position possible to put the text

    pyfiglet.format("text editor")
    print("Note: Since it's non gui we will ask you many question to place the text")

    path = str(input("Set the path of your picture : "))
    Image.open(path)
    text = str(input("Set the text you want : "))
    print("""set the front :
            1: Arial
            2: Impact
            4: Algerian
            5: Comic sans-serif
    """)

    font = int(input("font (1-6) : "))
    size = int(input("set the size of your text (50-300)"))

    if font == 1:
        font = ImageFont.truetype('playfair/playfair-font.ttf', size)
    elif font == 2:
        font = ImageFont.truetype('ressources/ttf/x.ttf')
    elif font == 3:
        font = ImageFont.truetype('ressources/ttf/x.ttf')
    elif font == 4:
        font = ImageFont.truetype('ressources/ttf/x.ttf')
    elif font == 4:
        font = ImageFont.truetype('ressources/ttf/x.ttf')
    else :
        print("wrong input, quitting")
        time.sleep(2)
        quit()
    
    position = str(input("Set the position of your picture (bottom, top, center) : "))
    r, g, b = int(input("Set rgb (enter 3 value")).spilt()
    output_path = str(input("Set the output path of the picture"))
    time.sleep(1)
    print("[*] Processing... \n")
    temp_edit = ImageDraw.Draw(path)
    print("[*] Putting text...")
    temp_edit.text((position), text, (r, g, b), font=font)
    temp_edit.save(output_path)
    print("[*] Done.")
    see = str(input("do you want to see the picture? y/n"))

    if see == "y":
        Image.show(output_path)
    elif see == "n":
        print("ok\n")
        print("[!] Quitting")
        quit()
    else:
        print("wrong input case sensitive y or n")

    #TODO: Maybe I should see if we can import stuff to do this because it will be pretty hard

while True:
    cmd = input(hostname+"@image_editor -> ").lower()

    if "help" in cmd:
        help()

    elif "clear" in cmd:
        os.system("clear")

    elif "upscale" in cmd:
        upscale()

    elif "bg" in cmd:
        bg() #call the function in the other file

    elif "exit" in cmd:
        quit()
    elif "x" in cmd:
        print("Add requests on Github...")
        time.sleep(1)
        print("") 
    elif "reize" in cmd:
        reize()

    elif "text" in cmd:
        text()
    elif cmd == "" or cmd == " ":
        print("please, type something.")
    else:
        print("wrong input")
        time.sleep(1)
        os.system("clear")
        time.sleep(1)
        print(banner)

        #REPORT ANY ISSUE ON GITHUB

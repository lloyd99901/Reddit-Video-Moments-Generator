#-----LunarHunter 2019-----#
#-----     Lloyd      -----#
import os
from PIL import Image
from selenium import webdriver
from selenium.webdriver.opera.options import Options
from time import sleep

def videotoavi(locallocation):
    os.system('ffmpeg -i ' + locallocation + ' -b 30000 -vb 20M -r 11 -vf "scale=1920:-1" generatedavi.avi > logs\\outputmp4.txt 2> logs\\errmp4.txt')

def genfinalvid():
    try:
        os.remove('final.mp4')
        os.remove('finalgen_video.mp4')
    except:
        print("Failed to remove final.mp4 and/or finalgen_video.mp4")
    filea = "file 'vidgen/question.avi'\n"
    fdata = open("list.txt", "w+")
    for filename in os.listdir("vidgen\\"):
        if 'question.avi' in filename:
            continue
        filea = filea + "file 'vidgen/" + filename + "'\n"
        filea = filea + "file 'GFX/123.avi'\n"
    fdata.write(filea)
    fdata.close()
    sleep(0.4)
    os.system("ffmpeg -f concat -i list.txt -c copy final.mp4 > logs\\output.txt 2> logs\\err.txt")
def combinesoundandvideo():
    counta = 0
    os.system('ffmpeg -i temp\\question1.png -i temp\\question.wav -af "apad=pad_dur=1" -b 30000 -vb 20M -r 11 -vf "scale=1920:-1" vidgen\\question.avi > logs\\outputmp4.txt 2> logs\\errmp4.txt')
    while counta < 30:
        print(str(counta))
        os.system('ffmpeg -i temp\\' + str(counta) + '.png -i temp\\' + str(counta) + '.wav -af "apad=pad_dur=1" -b 30000 -vb 20M -r 11 -vf "scale=1920:-1" vidgen\\' + str(counta) + '.avi > logs\\outputmp4.txt 2> logs\\errmp4.txt')
        counta = counta + 1

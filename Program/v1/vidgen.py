#-----LunarHunter 2019-----#
#-----     Lloyd      -----#
import os
#from PIL import Image
from time import sleep
from pathlib import Path
#def videotoavi(locallocation):
#    os.system('ffmpeg -i ' + locallocation + ' -b 30000 -vb 20M -r 11 -vf "scale=1920:-1" generatedavi.avi > logs\\outputmp4.txt 2> logs\\errmp4.txt')

def genfinalvid():
    try:
        os.remove('final.mp4')
    except:
        print("VidGen: Failed to remove final.mp4")
    filea = ""#"file 'GFX/audiofix.mp4'\n" #"file 'vidgen/question.avi'\n"
    i = 0
    while True:
        #This while loop is to fix a 'bug' where if the first video doesn't have sound, the rest of the videos don't have sound either, starting the video with a video with sound, it will fix the problem.
        if i == 100:
            print("VidGen: Int surpassed maximum allowed, exiting...")
            quit()
        if Path("downloads\\"+str(i) + ".mp3").stat().st_size == 243:
            print("VidGen: " + str(i) + ".mp3 is empty")
        else:
            filea = "file 'combined/" + str(i) + ".mp4'\n"
            break
        i = i + 1

    fdata = open("list.txt", "w+")
    for filename in os.listdir("combined\\"):
        if str(i) in filename:
            continue
        filea = filea + "file 'combined/" + filename + "'\n"
        filea = filea + "file 'GFX/123.avi'\n"
    fdata.write(filea)
    fdata.close()
    sleep(0.4)
    #os.system("ffmpeg -f concat -safe 0 -i list.txt -c copy final.mp4 > logs\\output.txt 2> logs\\err.txt")
    execfinalvidgeneration()
def combinesoundandvideo(video, audio, outputloc):
    os.system('ffmpeg -i ' + video + audio +' ' + outputloc + ' > logs\\outputmp4.txt 2> logs\\errmp4.txt')
def execfinalvidgeneration():
    os.system("ffmpeg -f concat -safe 0 -i list.txt -c copy final.mp4 > logs\\output.txt 2> logs\\err.txt")
genfinalvid()

#execfinalvidgeneration()

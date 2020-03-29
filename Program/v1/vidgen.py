#-----LunarHunter 2019-----#
#-----     Lloyd      -----#
import os
#from PIL import Image
from time import sleep

#def videotoavi(locallocation):
#    os.system('ffmpeg -i ' + locallocation + ' -b 30000 -vb 20M -r 11 -vf "scale=1920:-1" generatedavi.avi > logs\\outputmp4.txt 2> logs\\errmp4.txt')

def genfinalvid():
    try:
        os.remove('finalvideo.mp4')
    except:
        print("Failed to remove final.mp4")
    filea = "" #"file 'vidgen/question.avi'\n"
    fdata = open("list.txt", "w+")
    for filename in os.listdir("combined\\"):
        filea = filea + "file 'combined/" + filename + "'\n"
        filea = filea + "file 'GFX/123.avi'\n"
    fdata.write(filea)
    fdata.close()
    sleep(0.4)
    os.system("ffmpeg -f concat -safe 0 -i list.txt -c copy final.mp4 > logs\\output.txt 2> logs\\err.txt")
def combinesoundandvideo(video, audio, outputloc):
    os.system('ffmpeg -i ' + video + '' + audio +' ' + outputloc + ' > logs\\outputmp4.txt 2> logs\\errmp4.txt')

genfinalvid()

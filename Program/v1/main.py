#-----Lloyd 2019-----#
#-----LunarHunter-----#
#This script is under the The Unlicense license!

#TODO:
#Add a list of subreddits, script will grab videos from the randomly chosen subreddit

import os, sys, requests, json
from random import randint
from time import time, sleep
from subprocess import Popen as process
import vidgen
from pathlib import Path
total_time = time()
#answer = input('-----LunarHunter 2019-----\n-----Reddit Video Moments Generator-----\n\nPlease note the following:\nThis program is under the Unlicense license! I would suggest running in a VM to avoid any problems that prevents termination.\n\n' +   
#               'Please delete all files in temp and vidgen before running this program! I will add this feature soon but not currently a priority.\n' +
#               'The final video requires background music so manual editing is required\n\n' +
#               'Please indicate approval to running the program and agreeing to the terms of the license: [y/n]')
#if not answer or answer[0].lower() != 'y':
#    print('You did not indicate approval!')
#    sleep(2)
#    exit(1)

print("Declaring, setting and checking important vars\n")
#print(os.path.dirname(sys.argv[0]) + "\\wkhtmltoimage.exe")

#This is how far the script goes into posts before stopping
depthlimit = 20

randcom = []
videosToDownload = []

link = "https://www.reddit.com/r/WatchPeopleDieInside.json"

if depthlimit <=0 or link == "":
  print("A variable is invaild - ERROR")
  quit()
print("Done checking vars\n")

data = json.loads(requests.get(link, headers={"User-agent":"rb0.1"}).text)["data"]["children"]
print("Building question array...\n")
i = 0
for question in data:
    if i > depthlimit:
        break
    i = i + 1
    question = question["data"]
    randcom.append("https://www.reddit.com" + question["permalink"])
    
print("Building videosToDownload array...")
for selectedurl in randcom:
    data = json.loads(requests.get(selectedurl + ".json", headers={"User-agent":"rb0.1"}).text)[0]["data"]["children"]
    for answer in data:
        answer = answer["data"]
        if answer["over_18"] == True:
            print("Bypassing over 18 post.")
            continue
        videosToDownload.append(answer["secure_media"]["reddit_video"]["fallback_url"])

i = 0
for videoToDownload in videosToDownload:
    downloadvideo = requests.get(videoToDownload, stream = True)
    print(videoToDownload)
    with open("downloads\\" + str(i) + ".mp4","wb") as mp4:
        for chunk in downloadvideo.iter_content(chunk_size=1024):
            if chunk:
                mp4.write(chunk)

    print(videoToDownload.replace(videoToDownload.split("/")[4], ""))
    downloadaud = requests.get(videoToDownload.replace(videoToDownload.split("/")[4], "") + "audio", stream = True)
    with open("downloads\\" + str(i) + ".mp3","wb") as mp3:
        for chunk in downloadaud.iter_content(chunk_size=1024):
            if chunk:
                mp3.write(chunk)
    if Path("downloads\\" + str(i) + ".mp3").stat().st_size == 243:
      vidgen.combinesoundandvideo("downloads\\" + str(i) + ".mp4", "", "combined\\" + str(i) + ".mp4")
    else:
      vidgen.combinesoundandvideo("downloads\\" + str(i) + ".mp4", " -i downloads\\" + str(i) + ".mp3", "combined\\" + str(i) + ".mp4")
    i = i + 1

vidgen.genfinalvid()

# downloadtest = requests.get(videosToDownload[0], stream = True)

# print(videosToDownload[0])

# with open("test.mp4","wb") as mp4:
#     for chunk in downloadtest.iter_content(chunk_size=1024):
#         if chunk:
#             mp4.write(chunk)

# print(videosToDownload[0].replace(videosToDownload[0].split("/")[4], ""))

# downloadtestaud = requests.get(videosToDownload[0].replace(videosToDownload[0].split("/")[4], "") + "audio", stream = True)

# with open("test.mp3","wb") as mp3:
#     for chunk in downloadtestaud.iter_content(chunk_size=1024):
#         if chunk:
#             mp3.write(chunk)

#vidgen.combinesoundandvideo("test.mp4", "test.mp3", "testcom.mp4")

print("\n\nProgram finished! Total Time: " + round(time() - total_time, 2))

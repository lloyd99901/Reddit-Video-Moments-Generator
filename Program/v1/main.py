﻿#-----Lloyd 2019-----#
#-----LunarHunter-----#
#This script is under the The Unlicense license!

import os, sys, requests, json
from random import randint
from time import time, sleep
from subprocess import Popen as process
import vidgen
total_time = time()
answer = input('-----LunarHunter 2019-----\n-----Reddit Video Moments Generator-----\n\nPlease note the following:\nThis program is under the Unlicense license! I would suggest running in a VM to avoid any problems that prevents termination.\n\n' +   
               'Please delete all files in temp and vidgen before running this program! I will add this feature soon but not currently a priority.\n' +
               'The final video requires background music so manual editing is required\n\n' +
               'Please indicate approval to running the program and agreeing to the terms of the license: [y/n]')
if not answer or answer[0].lower() != 'y':
    print('You did not indicate approval!')
    sleep(2)
    exit(1)
start_time = time()


print("Declaring, setting and checking important vars\n")
#print(os.path.dirname(sys.argv[0]) + "\\wkhtmltoimage.exe")

#This is how far the script goes into comments before stopping
depthlimit = 15

randcom = []

link = "https://www.reddit.com/r/WatchPeopleDieInside.json"

if depthlimit <=0 or link == "":
  print("A variable is invaild - ERROR")
  quit()
print("Done checking vars\n")

data = json.loads(requests.get(link, headers={"User-agent":"rb0.1"}).text)["data"]["children"]
print("Building randcom array...\n")
i = 0
for question in data:
    if i > depthlimit:
        break
    i = i + 1
    question = question["data"]
    randcom.append("https://www.reddit.com" + question["permalink"])

for answer in randcom:
    

print("\n\nProgram finished!")

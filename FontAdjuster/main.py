import sys
import time

import androidstudio
import brave
import firefox
import intellijIdea
import process_manager
import spotify


# python3 main.py spotify:0 firefox:1.3 android_studio:14 intellij_idea:14 brave:1.2239010857415449

process_manager.closeApps([androidstudio.process, brave.process, firefox.process, intellijIdea.process, spotify.process])
time.sleep(1)

args = {}

for i in range(1, len(sys.argv)):
    split = sys.argv[i].split(":")
    args[split[0]] = split[1]


firefox.adjustFont(args['firefox'])
intellijIdea.adjustFont(args['intellij_idea'])
androidstudio.adjustFont(args['android_studio'])
brave.adjustFont(args['brave'])
spotify.adjustFont(args['spotify'])

print(args)
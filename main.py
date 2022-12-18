# Just import all you links into the 'links.txt' file with 1 link per line
# After that just run the program 
# And please do not change any of the code unless you know what u're doing :)


#Imports

import pyautogui
import time
import os

# Constants

BROWSER = 'chrome'        # Change this if you use another browser (remove the '#' from the one you are using and insert it on the one that doesn't have it)
#BROWSER = 'microsoftedge'
#BROWSER = 'opera'
# BROWSER = 'firefox'

# Code
links = []
lines = 0

with open('links.txt', 'r') as f: 
        lines = f.readlines()
        f.close()

with open('links.txt', 'r') as f:
    for line in lines:
        links.append(f.readline())
    f.close()

# Create a string from the links

count = 0
args = ''


for line in lines:
    args += links[count].replace('\n', '') + ' '
    count += 1

# Make a bat file to open the links in the browser. Run it and then delete the file

with open('open.bat', 'w') as f:
    f.write(f"start {BROWSER} {args}")
    f.close()

os.system('open.bat')
os.remove('open.bat')
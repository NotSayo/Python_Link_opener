# Just import all you links into the 'links.txt' file with 1 link per line
# After that just run the program 
# And please do not change any of the code unless you know what u're doing :)


#Imports
import pyautogui
import time
import json


# Browser

BROWSER = ''

with open ('Browser.json', 'r') as f: 
    file_json = json.loads(f.read())
    BROWSER = file_json["Browser"]
    
    while BROWSER not in ['chrome', 'microsoftedge', 'opera', 'firefox']:
        BROWSER = input('What browser do you use? (chrome, microsoftedge, opera, firefox): ')
    
    f.close()
    
with open ('Browser.json', 'w') as f: 
    dictionary = {"Browser" : f"{BROWSER}"}
    object = json.dumps(dictionary)
    f.write(object)
    
    f.close()
    

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
    
# Open cmd

pyautogui.keyDown('win')
pyautogui.press('r')
pyautogui.keyUp('win')
time.sleep(0.1)

# Create a string from the links

count = 0
args = ''


for line in lines:
    args += links[count].replace('\n', '') + ' '
    count += 1

# Open the links

pyautogui.typewrite(f"{BROWSER} {args}")
pyautogui.press('enter')
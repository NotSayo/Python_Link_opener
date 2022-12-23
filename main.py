# Just import all you links into the 'links.txt' file with 1 link per line
# After that just run the program 
# And please do not change any of the code unless you know what u're doing :)


#Imports

import os
import json

#Browser

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
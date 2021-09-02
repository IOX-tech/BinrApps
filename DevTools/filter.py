# Program for Encrypt all files

from os import walk
from time import sleep

PATH = "/home/phio/Documents/work/BinrApps/test_example" # Collect data Dynamically using studio.bind

files = []

files1 = next(walk(PATH),(None,None,[]))[2]

if PATH.endswith('/'):
    for file in files1:
        files.append(PATH+file)
else:    
    for file in files1:
        files.append(PATH+"/"+file)

# Examining the subfolders:

subdirs = [x[0] for x in walk(PATH)]
# print(subdirs)

for anyDir in subdirs:
    filenames = next(walk(anyDir), (None, None, []))[2]
    for filename in filenames:
        files.append(anyDir+"/"+filename)

# print(files)

filenames = files

python_files = []
html_files = []
css_files = []
js_files = []
binr_en = []
other_files = []

for file in filenames:
    if file.endswith(".py"):
        sleep(0.3)
        python_files.append(file)
        print(file,"is recognized as python code")
    elif file.endswith(".html"):
        sleep(0.4)
        print(file,"is recognized as HTML code")
        html_files.append(file)
    elif file.endswith(".css"):
        sleep(0.6)
        print(file,"is recognized as CSS code")
        css_files.append(file)
    elif file.endswith(".js") or file.endswith(".jsx"):
        sleep(0.4)
        print(file,"is recognized as JS code")
        js_files.append(file)
    elif file==("studio.bind"):
        sleep(0.8)
        print(file,"is recognized as Binr code")
        binr_en.append(file)
    else:
        sleep(1)
        print(file,"is recognized as OTHERS")
        other_files.append(file)

python_files,js_files,html_files,css_files,binr_en,other_files = list(set(python_files)),list(set(js_files)),list(set(html_files)),list(set(css_files)),list(set(binr_en)),list(set(other_files))

trash = []

for others in other_files:
    if others.endswith("studio.bind") or others.endswith(".json") or others.endswith(".txt") or others.endswith(".md"):
        pass
    else:
        trash.append(others)

for waste in trash:
    sleep(1)
    print("Could not recognize",waste,".File is been not included.")
    other_files.remove(waste)

other_files = other_files


# use from filter import *

# print(python_files,js_files,html_files,css_files,other_files)
# Program for Encrypt all files

from abc import abstractproperty
import os
import sys

from os import path,walk

outPATH = "/home/phio/Documents/work/BinrApps/client-scripts/core"

inPATH = "/home/phio/Documents/work/BinrApps/client-scripts/front"

filenames = next(walk(outPATH), (None, None, []))[2]

filenamesIn = next(walk(inPATH), (None, None, []))[2]

filenames.extend(filenamesIn)

print("Processing...")

default_files = (".py",".html",".css",".js","studio.bind")

python_files = []
html_files = []
css_files = []
js_files = []
binr_en = []
other_files = []

for file in filenames:
    if file.endswith(".py"):
        python_files.append(file)
    elif file.endswith(".html"):
        html_files.append(file)
    elif file.endswith(".css"):
        css_files.append(file)
    elif file.endswith(".js"):
        js_files.append(file)
    elif file==("studio.bind"):
        binr_en.append(file)
    else:
        other_files.append(file)

#Removing unwanted files
"ToDo"
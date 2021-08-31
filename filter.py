# Program for Encrypt all files

from abc import abstractproperty
import os
import sys

from os import path,walk

outPATH = None

inPATH = None # Collect data Dynamically using studio.bind

filenames = next(walk(outPATH), (None, None, []))[2]

filenamesIn = next(walk(inPATH), (None, None, []))[2]

filenames.extend(filenamesIn)

# print("Processing...")

# Remove unwanted Files...
default_files = (".py",".html",".css",".js",".bind",".json",".txt",".md")
for files in filenames:
    for df in default_files:
            if files.endswith(df):
                pass
            else:
                filenames.remove(files)


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

def args_py():
    for py_f in python_files:
        return py_f

def args_html():
    for hfi in html_files:
        return hfi

def args_css():
    for cf in css_files:
        return cf

def args_js():
    for jf in js_files:
        return jf

def args_oth():
    for of in other_files:
        return of

# use from filter import *
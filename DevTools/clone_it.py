# """
# Making a MKDIR
# ==> Putting all the FILES
# Making Executable out of it
# Run and Test
# """

import os
from __studio__ import formOn, wheeler_name

root = None

# Declaring default path
if formOn is None:
    PATH = ""
    print("Using output Directory as the Input Folder.")
else:
    PATH = formOn

PATH = PATH

if PATH.endswith("/"):
    pass
elif bin(PATH) == False:
    pass
else:
    PATH = PATH+"/"

os.system("mkdir",PATH+wheeler_name)
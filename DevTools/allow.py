from sys import platform

print("Recomended: Use an virtual machine for good packaging")

if platform == 'linux':
    pass # execute all shell files
else:
    print("Sorry! packaging does only work under Linux")
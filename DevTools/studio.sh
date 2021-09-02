#!/bin/sh

echo "Starting Binr Packager..."
echo "Enter studio.bind path here: "
read file
echo "Preparing to package " $file
echo "Making it prepared"
python3 wait.py
echo "Automated process. Donot Key Interupt."
python3 filter.py
file
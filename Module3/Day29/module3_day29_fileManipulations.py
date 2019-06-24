"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module3_day29_fileManipulations.py
    Creation Date:  6/21/2019, 7:12 PM
    Description:    Python Automation Program 1: File Manipulations
"""

import os

# First change the working directory to point to the folder containing the files
os.chdir(".\\audio")

# The `.listdir()` function populates the contents of the folder. This can be iterated over to work with the files.
for file in os.listdir():
    # The files contain the format `title_module_day_track.mp3`

    # The `os.path.splitext()` function separates the extension from the file name. This can be used to create a tuple
    # of the file name and the file extension.
    file_name, file_ext = os.path.splitext(file)

    # Since the folder can contain files other than `.mp3`, the program will be told to ignore all other extensions.
    if file_ext != ".mp3":
        continue

    # Similar to the method of splitting off the file extension, the title, module, day, and track can all be separated
    # into a tuple by splitting on the underscore.
    title, module, day, track = file_name.split("_")

    # The track number includes the number sign which isn't ideal and needs to be removed. Additionally, since there are
    # tracks in the double digits, the system will sort track 10 immediately after track 1. Therefore, padding also
    # needs to be applied using the `.zfill()` method to ensure proper order.
    track = track[1:].zfill(2)

    # The `.rename()` function can then be used to rename the file with the desired format.
    new_name = f"{track}-{title}{file_ext}"
    os.rename(file, new_name)

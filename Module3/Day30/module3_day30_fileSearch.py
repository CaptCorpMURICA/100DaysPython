"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module3_day30_fileSearch.py
    Creation Date:  6/24/2019, 11:05 AM
    Description:    Python Automation Program II: File Search
"""

import os

# The path of the parent folder intended to search
searchPath = ".\\election_2016"

# The search term for the query
searchTerm = input("What would you like to search for?\n")

# File extension
extension = ".txt"

try:
    os.chdir(searchPath)
except FileNotFoundError:
    print(f"{searchPath} is invalid. Current working directory is {os.getcwd()}")

# Create an empty list to store the file names
files = []

# Store files into the list
# Replace file type based on need
for dirpath, dirnames, filenames in os.walk("."):
    for filename in [f for f in filenames if f.endswith(extension)]:
        files.append(os.path.join(dirpath, filename))

# Iterate through each line in each file to look for a specified search term
for file in files:
    try:
        f = open(file, "r")
        searchLines = f.readlines()
        f.close()
        print("Start file {0}".format(file))
        for i, line in enumerate(searchLines):
            if searchTerm.lower() in line.lower():
                print("Line {0}: {1}".format(i, line.rstrip()))
        print("End file {0}".format(file))
        print("=" * 50)
    except FileExistsError:
        print("Error with file {0}.".format(file))
        print("=" * 50)
        continue
    except FileNotFoundError:
        print("Error with file {0}.".format(file))
        print("=" * 50)
        continue

print("End Script")

#a python program can be written to open and read a file to seach the embedded text for a keyword
#the election_2016 folder contains the hierarchy that contains various .csv, .txt, and .xlsx files

import os

#the path of the parent folder intended to search 
searchPath = "/Users/jchave621/100DaysPython/Module3/Day30/election_2016"

#the search term for the query 
searchTerm = input("What would you like to search for?\n")

#file extension
extension = ".txt"

try:
    os.chdir(searchPath)
except FileNotFoundError:
    print(f"{searchPath} is invalid. Current working directory is {os.getcwd()}")

#create an empty list to store the file names
files = []

#store the files into the list
#replace file type based on need 
for dirpath, dirnames, filenames in os.walk("."):
    for filename in [f for f in filenames if f.endswith(extension)]:
        files.append(os.path.join(dirpath, filename))

#iterate through each line in each file to look for a specified search term
for file in files:
    try:
        f = open(file, "r")
        searchLines = f.readlines()
        f.close()
        print("Start file {0}".format(file))
        for i, line in enumerate(searchLines):
            if searchTerm.lower() in line.lower():
                print("Line {0}: {1}".format(i, line.rstrip()))
        print("End file {0}.".format(file))
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
import os

# first change the working directory to point to the folder containing the files
os.chdir("/Users/jchave621/100DaysPython/Module3/Day29/audio")

# the listdir() function populates the contents of the folder. This can be iterated over to work with the files 
for file in os.listdir():
    # the files contain the format `title_module_day_track.mp3`

    # the `os.path.splitext()` function seperated the extension from the file name. 
    # this can be used to create a tuple of the file name and the file extenstion
    file_name, file_ext = os.path.splitext(file)

    # since the folder can contain files other than `mp3`, the program will be told to ignore all other extensions
    if file_ext != ".mp3":
        continue
    
    #similar to the method of splitting off the file extension, the title, mdoule, day and track can all be seperated 
    #into a tuple by splitting on the underscore
    title, module, day, track = file_name.split("_")

    #the track number includes the number sign which isn't ideal and needs to be removed. Additionally, since there are
    #tracks in the double digits, the system will sort track 10 immediately after track 1. Therefore, padding also
    #needs to be applied using the `.zfill()` method to ensure proper order.
    track = track[1:].zfill(2)

    #the `.rename()` function can then be used to rename the file with the desired format
    new_name = f"{track}--{title}{file_ext}"
    os.rename(file, new_name)
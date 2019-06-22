# Day 29: File Manipulations 
**Instructions:** 
1. Open a new python file.
2. Have you ever needed to manipulate a large number of files or repeatably update files to add consistency for a process? Often, I will download an entire course for offline consumption. Sometimes, these files are in a consistent format, but it's not in an ideal format for sequential viewing. Included, there are ten `.mp3` files that contain the module name, day name, track number, and extension. This is a clean format, but it may not play each sequential track in order. For this purpose, 2. Have you ever needed to manipulate a large number of files or repeatably update files to add consistency for a process? Often, I will download an entire course for offline consumption. Sometimes, these files are in a consistent format, but it's not in an ideal format for sequential viewing. Included, there are ten `.mp3` files that contain the track name, module name, day name, track number, and extension. This is a clean format, but it will not play in the proper order because the files are first sorted by the track name in alphabetical order. For this purpose, it would be preferable to have the format `track no - name.mp3`.
    ```
    import os

    # First change the working directory to point to the folder containing the files
    os.chdir(".\\Module3\\Day29")

    # The `.listdir()` function populates the contents of the folder. This can be iterated over to work with the files.
    for file in os.listdir():
        # The files contain the format `title_module_day_track.mp3` 
    
        # The `os.path.splitext()` function separates the extension from the file name. This can be used to create a tuple
        # of the file name and the file extension.
        file_name, file_ext = os.path.splitext(file)
        
        # Since the folder contains files other than `.mp3`, the program will be told to ignore all other extensions.
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
    ```
3. Update the [log file](../../log.md) with what you have learned today. 
# Day 30: File Search
**Instructions:** 
1. Open a new python file.
2. Every day, we use search functions on the computer or internet to greatly improve our experiences by finding the necessary information in the shortest possible time. File searches often do not comb through the text of a document before returning results. If you need to locate any file on the system that contains a specific keyword, the built in functionality will not meet your needs. However, a python program can be written to open and read a file to search the embedded text for the keyword. As an example, a collection of the [2016 election polls and speeches (collected by Alan Du)](https://www.kaggle.com/alandu20/2016-us-presidential-campaign-texts-and-polls) was uploaded to Kaggle. This has a folder hierarchy that contains various `.csv`, `.txt`, and `.xlsx` files.
3. By using the `os.walk()` method, the application can move through the directory tree to search through all subfolders. The program opens the `.txt` files, reads the contents into memory, and then loops through the lines to find the keyword provided. If found, the entire line is written to the terminal. This type of application is extremely useful if you need to review a server full of scripts to find the specific one that generates a file in question. The program is essentially a giant electromagnet to find a needle in a haystack.
    ```
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
    ```
2. Update the [log file](../../log.md) with what you have learned today.
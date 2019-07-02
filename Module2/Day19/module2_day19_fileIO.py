"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module2_day19_fileIO.py
    Creation Date:  6/8/2019, 6:05 PM
    Description:    Learn the basics of file input/output in python.
"""

# Before working with files, make sure to import the `os` package and change the directory to the desired location if
# required. In Python Enhancement Proposal (PEP) 20 an Easter Egg was added to python. By executing `import this`, the
# "Zen of Python" by Tim Peters is provided. This is a collection of aphorisms that succinctly describe the guiding
# principles of Python's design, according to Guido van Rossum (the Benevolent Dictator for Life).
import this
import os

print(os.getcwd())
os.chdir('./Module2/Day19')

# First we need to decrypt the "Zen of Python."
zen = ""
for letter in list(this.s):
    if letter in list(this.d.keys()):
        zen += this.d[letter]
    else:
        zen += letter
print(zen)

# By using the built-in `open()` function, a file can be created in the current working directory (cwd) to save the "Zen
# of Python" for future use. The `open(filename, mode)` function requires the first argument to contain the name of the
# file and the second argument is either `w` for write, `r` for read, and `a` for append. Once a file is no longer
# needed, the `.close()` method is required.
with open('zen.txt', 'w') as z:
    z.write(zen)
z.close()

# With the `r` option, an existing file can be read. Similar to the `w` option, the `.close()` method must be used after
# the file is no longer required. Additionally, the `.readline()` method produces the entire line of the file or a
# specific number of characters specified within the parentheses. For each instance of `.readline()`, a subsequent line
# in the file will be provided.
with open('declaration.txt', 'r') as d:
    print(d.readline())
    print(d.readline(25))
d.close()

# By using a for loop, all lines in the file can be written in a single operation. Using the `end=''` option, the
# default newline character is not used to eliminate adding a duplicate newline character.
with open('farewell.txt', 'r') as d:
    for lines in d:
        print(lines, end='')
d.close()

# The append status can be used to add additional content to an existing file. Once the file to be appended is open,
# the file to append can be opened in read status. The `file=` option within the print statement allows the content to
# printed to the open file. Since a file with an active append status cannot be read. The file must be closed and
# reopened in read status to confirm the action was successful.
# Read the file in the original state.
print("{:=^50}\n".format(" BEFORE APPEND "))
with open('constitution.txt', 'r') as c:
    for lines in c:
        print(lines, end='')
c.close()

# Appending action
with open('constitution.txt', 'a') as c:
    print('\n', file=c)
    with open('billofrights.txt', 'r') as b:
        for lines in b:
            print(lines, end='', file=c)
    b.close()
c.close()

# Confirmation of successful appending.
print("\n\n{:=^50}\n".format(" AFTER APPEND "))
with open('constitution.txt', 'r') as c:
    for lines in c:
        print(lines, end='')
c.close()

# The `rename()` function can be used to update the name of a file.
os.rename('constitution.txt', 'constitutionBillOfRights.txt')

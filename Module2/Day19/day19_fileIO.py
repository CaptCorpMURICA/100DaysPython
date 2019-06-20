import this 
import os

print(os.getcwd())
os.chdir('/Users/julian/100DaysPython/Module2/Day19')

#decrypt the "Zen of Python"
zen = ""
for letter in list(this.s):
    if letter in list(this.d.keys()):
        zen += this.d[letter]
    else:
        zen += letter
print(zen)
print("=" * 26)

#the open() function allows us to save a file for future use
#The open(filename, mode) function requires the first argument to contain the name of the file and the second argument is either w for write, r for read, and a for append
with open('zen.txt', 'w') as z:
    z.write(zen)
z.close()

#the r option reads an existing file
with open('declaration.txt', 'r') as d:
    print(d.readline())
    print(d.readline(25))
d.close()

#all lines can be written in a single operation
#using the end='' option, the newline character is not used to eliminate adding a duplicate newline character
with open('declaration.txt', 'r') as d:
    for lines in d:
        print(lines, end='')
d.close()

print("=\n" * 26)
#to add content from the bill of rights file to the constitution file: 
# 1) open the file to be appended using the read status
print("{:=^50}\n".format(" BEFORE APPEND "))
with open('constitution.txt', 'r') as c:
    for lines in c:
        print(lines, end='')
c.close()

#2) close and reopen the file in append status, then do your transformations
with open('constitution.txt', 'a') as c:
    print('\n', file=c)
    with open('billofrights.txt', 'r') as b:
        for lines in b:
            print(lines, end='', file=c)
    b.close()
c.close()

#3) since a file with an active append status cannot be read, close again and reopen in read status
print("\n\n{:=^50}\n".format(" AFTER APPEND "))
with open('constitution.txt', 'r') as c:
    for lines in c:
        print(lines, end='')
c.close()

#the rename function can be used to update the name of a file
os.rename('constitution.txt', 'constitutionBillOfRights.txt')

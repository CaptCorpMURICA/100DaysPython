"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module2_day28_challenge_soln.py
    Creation Date:  6/2/2019, 8:55 AM
    Description:    Create a program to encrypt and decrypt messages using a substitution cipher. The user provides a
                    word that does not have any duplicate letters and no numbers or special characters. The user then
                    provides the instruction to either encrypt or decrypt the message. Finally, the user then provides
                    the message to be encrypted or decrypted. Create a function to check if the transposition word is
                    valid, another function to encrypt the message, and a third function to decrypt the message. When
                    encrypting the message, only letters should be provided; do not return any spaces, numbers, or
                    special character. Additionally, the program should not be case sensitive and all output should be
                    in lowercase. Create a testing program to validate the application works as designed. A substitution
                    cipher is created by shifting the letters of the alphabet based on a keyword. For instance, if the
                    word provided is "zebra", the cipher would be:
                    {"a": "z",
                     "b": "e",
                     "c": "b",
                     "d": "r",
                     "e": "a",
                     "f": "c",
                     "g": "d",
                     etc.}
"""

# Convert loop into a function
# Automatically remove special characters instead of breaking the program.

s = str(input("What is the code word?"))
for letter in s:
    if letter.lower() not in 'abcdefghijklmnopqrstuvwxyz':
        print("Only letters are allowed in the code word. {} is not an acceptable entry.".format(letter))
        break
    if s.count(letter) > 1:
        print("Invalid code word. There are {} {}s. There cannot be more than one instance of a letter in the code word"
              ".".format(s.count(letter), letter))
        break

# Create cipher here

while True:
    choice = input("""Options:
        1: Encrypt
        2: Decrypt
        3: Quit""")
    if choice == "1":
        pre_encrypt = input("What is the message to encrypt? ")
    elif choice == "2":
        pre_decrypt = input("What is the message to decrypt? ")
    elif choice == "3":
        print("Have a great day.")
        break
    else:
        print("{} is not a valid option. Try again.".format(choice))
        continue


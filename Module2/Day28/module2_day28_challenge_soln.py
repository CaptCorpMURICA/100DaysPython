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
                    in lowercase. Finally, add robust logging to collect insights about the effectiveness of the
                    application.

                    A substitution cipher is created by shifting the letters of the alphabet based on a keyword. For
                    instance, if the word provided is "zebra", the cipher would be:
                    {"a": "z",
                     "b": "e",
                     "c": "b",
                     "d": "r",
                     "e": "a",
                     "f": "c",
                     "g": "d",
                     etc.}
"""
import logging


def cipher_generator(password: str) -> dict:
    """
    Tests the keyword provided by the user for acceptable formatting. If approved, generates the cipher for the
    application.
    :param password: String input from the user.
    :return: Returns a list of tuples that contains pairs of the unscrambled alphabet with the encrypted alphabet.
    """
    alphabet = list("abcdefghijklmnopqrstuvwxyz")

    converted = []

    for letter in password:
        if password.count(letter) > 1:
            logger.error(f"The password cannot have any duplicate letters. {password} has "
                         f"{password.count(letter)} {letter}'s. Please try again.")
            raise KeyError(f"The password cannot have any duplicate letters. {password} has "
                           f"{password.count(letter)} {letter}'s. Please try again.")
        elif letter not in "abcdefghijklmnopqrstuvwxyz":
            logger.debug(f"The character, {letter}, was removed from the password.")
            continue
        else:
            converted.append(letter)

    logger.debug(f"The password ({''.join(str(l) for l in converted)}) was accepted. Building cipher.")

    for l in converted:
        alphabet.remove(l)

    converted.extend(alphabet)

    cipher = dict(zip(list("abcdefghijklmnopqrstuvwxyz"), converted))
    logger.debug(f"The cipher was created successfully:\n{cipher}")
    print("Password Accepted")
    return cipher


def encrypt_msg(msg: list, cipher: dict) -> str:
    """
    Accepts the message to be encrypted by the user, removes all characters except letters, encrypts the message and
    returns the result as a string.
    :param msg: List object that contains the message with only letters in lower case
    :param cipher: A dictionary object that contains the standard alphabet as the keys and the encrypted alphabet as the
                   values.
    :return: The received message after being encrypted and returned in string format with only letters.
    """
    encrypted = []

    for letter in msg:
        encrypted.append(cipher[letter])

    encrypted_msg = ''.join(str(l) for l in encrypted)
    logger.debug(f"Encryption completed successfully.\n{encrypted_msg}")
    return encrypted_msg


def decrypt_msg(msg: list, cipher: dict) -> str:
    """
    Accepts the message to be decrypted by the user, removes all characters except letters, decrypts the message and
    returns the result as a string.
    :param msg: List object that contains the message with only letters in lower case
    :param cipher: A dictionary object that contains the standard alphabet as the keys and the encrypted alphabet as the
                   values.
    :return: The received message after being decrypted and returned in string format with only letters.
    """
    decrypted = []

    for letter in msg:
        decrypted.append(list(cipher.keys())[list(cipher.values()).index(letter)])

    decrypted_msg = ''.join(str(l) for l in decrypted)
    logger.debug(f"Decryption completed successfully.\n{decrypted_msg}")
    return decrypted_msg


# Create the logger for the application
log_formatter = "%(levelname)s: %(asctime)s - %(message)s"
logging.basicConfig(filename="module2_day28_logging.log",
                    level=logging.DEBUG,
                    format=log_formatter,
                    filemode="w")
logger = logging.getLogger()
logger.info("Begin Program")

password = str(input("What is the password?\n")).lower()
logger.info(f"The password received was: {password}")
cipher = cipher_generator(password=password)

try:
    mode = input("What would you like to do?\n\t1: Encrypt Message\t2: Decrypt Message\t3: Enter a New Password\t4: "
                 "Quit\n").strip()
    logger.info(f"The user selected the mode: {mode}")
except KeyboardInterrupt as err:
    logger.error(f"Program manually closed by user through keyboard interrupt.\n{err}")
    raise
else:
    while mode != "4":
        if mode == "0":
            mode = input("What would you like to do?\n\t1: Encrypt Message\t2: Decrypt Message\t3: Enter a New Password"
                         "\t4: Quit\n").strip()
            logger.info(f"The user selected the mode: {mode}")
        elif mode == "1":
            msg = []
            message = str(input("What is the message for encryption?\n")).lower()
            logger.info(f"The user provided the message: {message}")
            for m in message:
                if m not in "abcdefghijklmnopqrstuvwxyz":
                    logger.debug(f"The character, {m}, was removed from the message.")
                    continue
                else:
                    msg.append(m)
            logger.info(f"Begin Encryption\nMessage: {msg}\nCipher: {cipher}")
            encrypted_msg = encrypt_msg(msg=msg, cipher=cipher)
            print(f"Your encrypted message is: {encrypted_msg}")
            mode = "0"
        elif mode == "2":
            msg = []
            message = str(input("What is the message for decryption?\n")).lower()
            logger.info(f"The user provided the message: {message}")
            for m in message:
                if m not in "abcdefghijklmnopqrstuvwxyz":
                    logger.debug(f"The character, {m}, was removed from the message.")
                    continue
                else:
                    msg.append(m)
            logger.info(f"Begin Decryption\nMessage: {msg}\nCipher: {cipher}")
            decrypted_msg = decrypt_msg(msg=msg, cipher=cipher)
            print(f"Your decrypted message is: {decrypted_msg}")
            mode = "0"
        elif mode == "3":
            password = str(input("What is the new password?\n")).lower()
            logger.info(f"The user provided the password: {password}")
            cipher = cipher_generator(password=password)
            mode = "0"
        elif mode == "4":
            logger.info("User Initiated Quit")
        else:
            logger.error(f"Invalid option received. {mode} is an invalid option.")
            print(f"{mode} is an invalid entry. Options are either 1, 2, 3, or 4.")
            mode = "0"
finally:
    print("Thank you for protecting your messages. Have a great day.")

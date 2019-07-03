"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module3_day37_mouseKeyboard.py
    Creation Date:  7/2/2019, 8:17 PM
    Description:    Python Automation Program 8: Mouse/Keyboard Manipulations
"""

# Anytime a program takes charge of the computer, it's critical that the user has a way to terminate the program. The
# `pyautogui` package has a `.PAUSE` variable that can be set with the number of seconds the program will wait after
# performing its action. Additionally, there is the `.FAILSAFE` variable that controls the option to force quit the
# program by moving the mouse to the upper-left corner of the screen.
import pyautogui
import subprocess
import sys
import time

pyautogui.PAUSE = 0.5
pyautogui.FAILSAFE = True

# Execute the command to open the file and perform a sleep action to ensure the application has opened before
# continuing. Depending on the hardware of the machine, the `.sleep()` timer can be extended or contracted.
sys_platform = sys.platform

if sys_platform == "win32" or sys_platform == "cygwin":
    subprocess.Popen(["start", ".\\ResumeTemplate.docx"], shell=True)
elif sys_platform == "darwin":
    subprocess.Popen(["open", ".\\ResumeTemplate.docx"])
elif sys_platform == "linux":
    subprocess.Popen(["see", ".\\ResumeTemplate.docx"])
else:
    print(f"Unknown operating system: {sys_platform}")

time.sleep(10)

# After launching the Word file to be converted to a PDF, focus needs to be applied to the application. The application
# first sends an `f12` command to try and open the `Save As` dialog box. If `pyautogui` locates the file type field by
# using an image of the option and the `.locateOnScreen` function, then the program continues. Otherwise, it locates the
# Microsoft Word icon on the taskbar and clicks on it. Once the focus is confirmed, the program selects the file type
# field and types `p d f` and then presses enter once to accept the file type and a second time to save. Since the
# `.locateOnScreen()` function returns more information than required for the `.click()` function, the `.center()`
# function is used to only return the `left` and `top` values.
try:
    pyautogui.press("f12")
    time.sleep(3)
    type_location = pyautogui.locateOnScreen(".\\icons\\TypeField.png")
    if type_location is None:
        try:
            word_icon = pyautogui.locateOnScreen(".\\icons\\WordLogo.png")
            word = pyautogui.center(word_icon)
            pyautogui.click(word)
        except TypeError:
            print("Word not found")
            raise
        else:
            pyautogui.press("f12")
            time.sleep(3)
except TypeError:
    print("Save not found")
    raise
else:
    type_loc = pyautogui.center(type_location)
    pyautogui.click(type_loc)

    pyautogui.typewrite(["p", "d", "f"])
    pyautogui.press(["enter", "enter"])

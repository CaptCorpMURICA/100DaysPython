# Day 37: Mouse/Keyboard Manipulations
**Instructions:** 
1. Open a new python file.
2. Python can connect to programs and websites using developer APIs; however, what happens if an API isn't available? The [pyautogui](https://pyautogui.readthedocs.io/en/latest/) package enables python to control the mouse and keyboard. In order to save a file as a PDF, the easiest solution is to automate the `Save As` process from within the native app.
3. Anytime a program takes charge of the computer, it's critical that the user has a way to terminate the program. The `pyautogui` package has a `.PAUSE` variable that can be set with the number of seconds the program will wait after performing its action. Additionally, there is the `.FAILSAFE` variable that controls the option to force quit the program by moving the mouse to the upper-left corner of the screen.
    ```
    import pyautogui
    import subprocess
    import sys
    import time

    pyautogui.PAUSE = 1.5
    pyautogui.FAILSAFE = True
    ```
4. Execute the command to open the file and perform a sleep action to ensure the application has opened before continuing. Depending on the hardware of the machine, the `.sleep()` timer can be extended or contracted.
    ```
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
    ```
5. After launching the Word file to be converted to a PDF, focus needs to be applied to the application. The application first sends an `f12` command to try and open the `Save As` dialog box. If `pyautogui` locates the file type field by using an image of the option and the `.locateOnScreen` function, then the program continues. Otherwise, it locates the Microsoft Word icon on the taskbar and clicks on it. Once the focus is confirmed, the program selects the file type field and types `p d f` and then presses enter once to accept the file type and a second time to save. Since the `.locateOnScreen()` function returns more information than required for the `.click()` function, the `.center()` function is used to only return the `left` and `top` values.
    ```
    try:
        pyautogui.press("f12")
        time.sleep(2)
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
                time.sleep(2)
    except TypeError:
        print("Save not found")
        raise
    else:
        type_loc = pyautogui.center(type_location)
        pyautogui.click(type_loc)

        pyautogui.typewrite(["p", "d", "f"])
        pyautogui.press(["enter", "enter"])
    ```
6. Update the [log file](../../log.md) with what you have learned today.

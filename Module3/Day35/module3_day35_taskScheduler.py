"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module3_day35_taskScheduler.py
    Creation Date:  6/30/2019, 2:00 PM
    Description:    Python Automation Program 7: Task Scheduler
"""

# The `subprocess` package is used to open and run external programs using python. While the `webbrowser.open()`
# function is used specifically to open a web browser and navigate to a specific web page, the `subprocess.Popen()`
# function is used for opening a specific application. This function can even be used to open and run another python
# script.
import subprocess

python_path = "<PATH TO THE PYTHON EXECUTABLE FILE>"
subprocess.Popen([python_path, "greeting.py"])

# Additionally, the `.Popen()` function can use the system defaults applications based on the file to be opened.
# Depending on the operating system, the method to call the file changes. Windows uses `start` and `shell=True`. OS X
# uses `open` and Linux uses `see`.
import sys

sys_platform = sys.platform

if sys_platform == "win32" or sys_platform == "cygwin":
    subprocess.Popen(["start", "..\\..\\Module2\\Day19\\declaration.txt"], shell=True)
elif sys_platform == "darwin":
    subprocess.Popen(["open", "..\\..\\Module2\\Day19\\declaration.txt"])
elif sys_platform == "linux":
    subprocess.Popen(["see", "..\\..\\Module2\\Day19\\declaration.txt"])
else:
    print(f"Unknown operating system: {sys_platform}")

# These functions can be combined with the `time` package to create an embedded task scheduler.
import time

try:
    sleep_time = float(input("How many minutes should the timer last?\n")) * 60
except TypeError:
    print(f"{sleep_time} is not a valid entry.")
    raise
except KeyboardInterrupt:
    print("The program was cancelled by the user.")
else:
    time.sleep(sleep_time)
    subprocess.Popen(["start", "alarm.mp3"], shell=True)
finally:
    print("Goodbye")

"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           greeting.py.py
    Creation Date:  6/30/2019, 3:03 PM
    Description:    Greeting program to say hello
"""

import os
from tkinter import messagebox
import time

username = os.getlogin()

if 5 <= time.localtime().tm_hour < 12:
    time_of_day = "morning"
elif 12 <= time.localtime().tm_hour < 17:
    time_of_day = "afternoon"
elif 17 <= time.localtime().tm_hour < 21:
    time_of_day = "evening"
else:
    time_of_day = "night"

greeting = f"Good {time_of_day}, {username}. Everything is going extremely well."

messagebox.showinfo("H.A.L. 9000", greeting)

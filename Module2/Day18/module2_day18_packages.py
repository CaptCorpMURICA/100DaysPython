"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module2_day18_packages.py
    Creation Date:  6/7/2019, 11:45 AM
    Description:    Learn the foundation of packages in python.
"""
# [built-in functions](https://docs.python.org/3/library/functions)
# [standard library](https://docs.python.org/3/library/library)
# [Turtle graphics](https://docs.python.org/3/library/turtle.html)

# All of the modules and functions used to this point are part of the python built-in functions. However, python is an
# open-source programming language, so incredibly smart people have created custom packages that do incredibly cool
# things. Python also includes the "standard library" which contains a set of packages already installed. Packages can
# be used in scripts through using the `import` statement. The `dir()` function can be used to display all of the
# built-in functions.
for func in dir(__builtins__):
    print(func)

# The packages in the standard library add extended functionality without needing to install new packages. After
# importing the package, the functions of the package can be used. The name of the package needs to be called in order
# to access the embedded functions. According to the PEP 8 formatting standards, all import declarations should occur at
# the top of the python file.
import random

num = random.randint(0, 100)
for i in range(0, 3):
    try:
        guess = int(input("Guess a number between 0 and 100: "))
    except:
        print("Please enter a valid integer between 0 and 100.")
        break
    if guess == num:
        print("{} is the correct value. You win.".format(guess))
    elif guess < num:
        print("{} is lower than the value. You have {} tries left.".format(guess, 2 - i))
    elif guess > num:
        print("{} is higher than the value. You have {} tries left.".format(guess, 2 - i))
    else:
        print("Something went wrong.")

# The `turtle` package is a fun way to get kids into programming. The user can give commands to a virtual turtle to
# instruct it to draw objects on screen.
import turtle
jonathan = turtle.Turtle()
jonathan.shape("turtle")
jonathan.forward(100)
jonathan.right(90)
jonathan.forward(100)
jonathan.right(90)
jonathan.forward(100)
jonathan.right(90)
jonathan.forward(100)
turtle.done()

# The `webbrowser` package allows interaction with an external web browser by using python. The system default browser
# will be used to launch the content first, but a specific browser can be specified for the task. Additionally, the
# built-in `help()` function can be used to print the documentation of the package specified in the terminal window.
import webbrowser

webbrowser.open("https://docs.python.org/3/library/webbrowser.html")
chrome = webbrowser.get(using='google-chrome')
chrome.open_new("https://www.youtube.com/watch?v=CMNry4PE93Y")
help(webbrowser)

# The `time` package is extremely useful for most software development. When doing performance testing, this package can
# provide insights on the bottlenecks of the script.
import time
start = time.time()
print("Program Start")
time.sleep(5)
print("Program End. The total execution time was {} sec.".format(time.time() - start))

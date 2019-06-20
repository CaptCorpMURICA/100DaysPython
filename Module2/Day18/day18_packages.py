#the dir() function can be used to display all of the built-in function
for func in dir(__builtins__):
    print(func)

# import random
# num = random.randint(0, 100)
# for i in range(0, 3):
#     try:
#         guess = int(input("Guess a number between 0 and 100: "))
#     except: 
#         print("Please enter a valid integer between 0 and 100.")
#         break
#     if guess == num:
#         print("{} is the correct valie. You win.".format(guess))
#     elif guess < num:
#         print("{} is lower than the value. You have {} tries left.".format(guess, 2 - i))
#     elif guess > num:
#         print("{} is higher than the value. You have {} tries left.".format(guess, 2 - i))
#     else:
#         print("Something went wrong.")

#the webbrowser package allows interaction with an external web brower
# import webbrowser
# print(webbrowser._browsers)
# url = 'http://docs.python.org/'
# chrome_path = 'open -a /Applications/Google\ Chrome.app %s'
# webbrowser.get(chrome_path).open(url)
 
import webbrowser
webbrowser.open_new("https://docs.python.org/3/library/webbrowser.html")
webbrowser.open_new_tab("https://www.youtube.com/watch?v=CMNry4PE93Y")
help(webbrowser)

# webbrowser.open("https://docs.python.org/3/library/webbrowser.html")
# webbrowser.get(chrome_path).open_new("https://www.youtube.com/watch?v=CMNry4PE93Y")

#the time package is used for performance testing 
import time
start = time.time()
print("Program Start")
time.sleep(5)
print("Program End. The total execution time was {} sec.".format(time.time() - start))

#the datetime package is more advanced than the time package, allows ability to manipulate dates
from datetime import datetime
print(datetime.today())
print("Day: {}\n Month: {}\n Year: {}".format(datetime.today().day, datetime.today().month, datetime.today().year))
if datetime.today() > datetime(datetime.today().year, 7, 4):
    days_until = (datetime(datetime.today().year + 1, 7, 4) - datetime.today()).days
    age = (datetime.today().year+ 1) - 1776
else: 
    days_until = (datetime(datetime.today().year, 7, 4) - datetime.today()).days
    age = datetime.today().year - 1776
print("There are {} days left until MURICA's birthday. MURICA will be {} years old.".format(days_until, age))

#the os package accesses the operating system 
import os 
print(os.getcwd())
# print(os.cpu_count())
print(os.getlogin())

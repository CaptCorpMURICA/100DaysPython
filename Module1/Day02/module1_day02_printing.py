"""
    Author:         Ben Carlson
    Project:        100DaysPython
    File:           module1_day02_printing.py
    Creation Date:  2019-06-03
    Description:    Learning how to print in python
"""

print("Hello World")

print("Hello" + " " + "World")

print("Rudy " * 5)

print("Ew\n\tWhat do you mean 'Ew'? I don't like spam.")

print(1 + 1)

# print("This is the answer to life, the universe, and everything: " + 42)

print("This is the answer to life, the universe, and everything: " + str(42))

print("The number of the {} shall be {}. No more. No less".format("counting", 3))

print(f"The number of the {'counting'} shall be {3}. No more. No less")

print("The number of the {1} shall be {0}. No more. No less".format(3, "counting"))

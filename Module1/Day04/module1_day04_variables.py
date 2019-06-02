"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module1_day04_variables.py
    Creation Date:  6/2/2019, 8:55 AM
    Description:    Learn about using variables in python.
"""

# Variables need to start with a letter or an underscore. Numbers can be used in the variable name as long as it is not
# the first character. Additionally, python is case sensitive, so the same word can store multiple items as long as the
# casing differs.
greeting = "Hello"
_name = "General Kenobi."
Greeting = "There"
_bestLine_ep3_ = "You are a bold one."
# Using string concatenation:
print(greeting + " " + Greeting + "\n\t" + _name + " " + _bestLine_ep3_)
# Using string replacement:
print("{} {}\n\t{} {}".format(greeting, Greeting, _name, _bestLine_ep3_))

# Variables can also store numeric values.
released = 2005
# Using string concatenation:
print("Revenge of the Sith was released on May 4, " + str(released) + ".")
# Using string replacement:
print("Revenge of the Sith was released on May 4, {}.".format(released))

# Variables are commonly used in arithmetic operations.
a = 3
b = 4
c = a ** 2 + b ** 2
print("Pythagorean Theorem: a^2 + b^2 = c^2, so when a = {} and b = {}, then c = {}".format(a, b, c))

# You can test for contents in a variable. If the test results **True**, then the tested condition is in the variable.
# Otherwise, the test returns **False**.
film = "Revenge of the Sith"
print("Sith" in film)
print("sith" in film)
print("sith" in film.lower())

# Python variables get their type with the data that is stored. Unlike other programming languages, you do not declare a
# type for the variable. Additionally, the same variable can be overwritten with new data and a different type. This
# should be taken into account when creating python programs.
var = "Variables are mutable"
type(var)
var = 3
type(var)
var = 3.5
type(var)

# If the variable contains a numeric value, it can be converted to an integer type with the int() function.
var = int(var)
type(var)

# The variable can be converted to a string with the str() function regardless of the contents.
var = str(var)
type(var)

# If the variable contains a numeric value, it can be converted to an float type with the float() function.
var = float(var)
type(var)
var = True
type(var)

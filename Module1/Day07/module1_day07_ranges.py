"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module1_day07_ranges.py
    Creation Date:  6/2/2019, 8:55 AM
    Description:    Basic instruction of ranges in python.
"""

# A range starts with an index of 0 and ends with the declared value. The endpoint of a range in not inclusive.
# Therefore, the range will contain indices from 0 to 41, but it will not use 42.
print(range(10))
print(list(range(10)))
print(range(0, 9, 2) == range(0, 10, 2))
# The range declaration has the format `range(start, stop, step)`.
even = range(0, 10, 2)
odd = range(1, 10, 2)
print("The even range is {} and the values are {}".format(even, list(even)))
print("The odd range is {} and the values are {}".format(odd, list(odd)))
# If the step is negative, then the range values are produced in reverse. The higher number must be in the start
# position if producing results in reverse.
even = range(10, 0, -2)
odd = range(9, 0, -2)
print("The even range is {} and the values are {}".format(even, list(even)))
print("The odd range is {} and the values are {}".format(odd, list(odd)))
# By using a specific step value, a range can be used to identify a collection of numbers divisible by a specific value.
# This example uses the `input()` function to prompt the user for input. It also used `if/elif/else` statements, which
# will be covered on [Day 10](../Module1/Day10).
val = int(input("Please provide a whole number for the divisibility check: "))
request = int(input("Please provide a whole number, less than 1 million, that is to be tested for divisibility: "))
in_range = range(val, 1000000, val)
if request > 1000000:
    print("Please select a number less than 1 million and try again. Thank you")
elif request in in_range:
    print("{} is divisible by {}.".format(request, val))
else:
    print("{} is not divisible by {}.".format(request, val))

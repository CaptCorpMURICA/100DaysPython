"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module1_day09_slicing.py
    Creation Date:  6/2/2019, 8:55 AM
    Description:    Learn the basics of slicing in python.
"""

# Specific items can be retrieved from a list by using its indices. _Type and execute:_
quotes = ["Pitter patter, let's get at 'er", "Hard no!", "H'are ya now?", "Good-n-you?", "Not so bad.",
          "Is that what you appreciates about me?"]
print(quotes[0])
print(f"{quotes[2]}\n\t{quotes[3]}\n{quotes[4]}")
# Slicing uses the format `[start:stop:step]`. Start is inclusive, but stop is exclusive. Unlike using just the index,
# slicing allows the user to return a sequence rather than a single item. Slicing can be conducted on mutable and
# immutable objects.
print(quotes[2:5])
# The step can be used to identify how many items to skip between returned values.
print(quotes[::2])
# The step can also be used to reverse the order of the returned items.
print(quotes[::-1])
# Slicing can be combined with indices to return a sequence from a specific item.
print(quotes[0][::2])
print(quotes[0][::-1])
# Slicing doesn't only need to be applied to lists. It can also be used on variables.
wayne = "Toughest Guy in Letterkenny"
print(wayne[::-1])
# Retrieval by index and slicing can also be applied directly to a string.
print("That's a Texas sized 10-4."[0:9:2])
# Neither the start, nor the stop values are required when slicing.
print(quotes[:])
print(quotes[3:])
print(quotes[:3])
print(quotes[::3])
# New list can be created based on the slicing output.
exchange = quotes[2:5]
print(exchange)

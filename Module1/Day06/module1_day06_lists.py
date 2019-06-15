"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module1_day06_lists.py
    Creation Date:  6/2/2019, 8:55 AM
    Description:    Learn the basic of lists in python.
"""

# There are two methods for creating an empty list.
list_1 = []
list_2 = list()
print("List 1 Type: {}\nList 2 Type: {}".format(type(list_1), type(list_2)))
# The `list()` function creates a list where each character is a separate entry.
text = "Luggage Combination"
print(list(text))
# The `.sort()` method is used to sort a list.
luggage = [1, 3, 5, 2, 4]
luggage.sort()
print(luggage)
# Variables built off a list are treated as the same object. For instance, if a sort is applied to a variable created
# from a list, the sort is also applied to the original.
numbers = [1, 2, 3, 4, 5]
numbers_sorted = numbers
numbers_sorted.sort(reverse=True)
print("numbers: {}\nnumbers_sorted: {}".format(numbers, numbers_sorted))
# In order to create a new version, a function needs to be called on the original list when creating a new one.
numbers = [1, 2, 3, 4, 5]
numbers_sorted = list(numbers)
numbers_sorted.sort(reverse=True)
print("numbers: {}\nnumbers_sorted: {}".format(numbers, numbers_sorted))
# Lists are easily able to be combined using a simple `+` operator.
odd = [1, 3, 5]
even = [2, 4]
luggage = odd + even
print(luggage)
# Lists can also be combined using the `.extend()` method.
luggage = [1, 3, 5]
even = [2, 4]
luggage.extend(even)
print(luggage)
# There are also several methods to sort the list.
odd = [1, 3, 5]
even = [2, 4]
luggage = odd + even
print("Unsorted list: {}".format(luggage))
print("Using the sorted() function: {}".format(sorted(luggage)))
luggage.sort()
print("Using the .sort() method: {}".format(luggage))
# Additional items can be added to a list by using the `.append()` method.
lines = list()
lines.append("They told me to comb the desert, so I'm combing the desert")
lines.append("YOGURT! I hate Yogurt! Even with strawberries!")
lines.append("We'll meet again in Spaceballs 2: The Quest for More Money.")
print(lines)
# The index of a requested item can be obtained using the `.index()` method.
luggage = [1, 2, 3, 4, 5]
print(luggage.index(2))
# The frequency of an item in a list can be obtained by using the `.count()` method. This is case sensitive.
quote = list("YOGURT! I hate Yogurt! Even with strawberries!")
print(quote.count("r"))
# The `.insert(index, item)` method can be used to add a new item to the list at a specific position.
luggage = [1, 2, 4, 5]
luggage.insert(2, 3)
print(luggage)
# The `.pop(i)` method can be used to remove and return the final element, or from a specific index `i`.
luggage = [1, 2, 3, 3, 4, 5, 6]
luggage.pop()
print(luggage)
luggage.pop(2)
print(luggage)
# The `.remove(i)` method eliminates a specific item (`i`) from the list.
rng = list(range(0, 10))
rng.remove(7)
print(rng)
# The `.reverse()` method reverses the order of the items in the list.
countdown = [5, 4, 3, 2, 1]
countdown.reverse()
print(countdown)
# Python can conduct transformations to a list while declaring a new list.
sample = list(range(1, 13))
times_12 = [i * 12 for i in sample]
print(times_12)
# A list can be cleared by using the `.clear()` method.
luggage.clear()
print(luggage)
# Since lists are mutable, items can be changed.
luggage = [2, 2, 3, 4, 5]
luggage[0] = 1
print(luggage)

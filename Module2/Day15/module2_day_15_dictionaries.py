"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module2_day_15_dictionaries.py
    Creation Date:  6/2/2019, 9:38 AM
    Description:    Learn the fundamentals of dictionaries in python.
"""

# Dictionaries are extremely useful objects that allow the user to map values to a specific key. These values can be
# returned simply by calling the key. This makes dictionaries not only useful, but also efficient. A dictionary is
# declared by using curly brackets (`{}`) and separating the key from the value with a colon (`:`). In order to call the
# value, the key is referenced in square brackets (`[]`) appended to the name of the dictionary.
conversion = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(conversion)
print(conversion["a"])

# Dictionaries require the key to be a single item, but the value can be a list of multiple items.
menu = {"item1": ["egg", "spam", "bacon"],
        "item2": ["egg", "sausage", "bacon"],
        "item3": ["egg", "spam"],
        "item4": ["egg", "bacon", "spam"],
        "item5": ["egg", "bacon", "sausage", "spam"],
        "item6": ["spam", "bacon", "sausage", "spam"],
        "item7": ["spam", "egg", "spam", "spam", "bacon", "spam"],
        "item8": ["spam", "egg", "sausage", "spam"]}
print(menu["item1"])
print(type(menu["item7"]))

# Since the value in the `menu` dictionary is a list, it can be changed in the same methodology as a normal list. By
# using slicing in conjunction with the key, specific items in the list can be retrieved and modified.
menu["item2"][2] = "spam"
print(menu["item2"])

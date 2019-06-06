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

# Lists are ordered collections of content, but dictionaries are not. In a dictionary, the key/value pairs can be added
# in any order. As long as the key/value pairs match between two dictionaries, python will interpret both to be the
# same.
# List Comparison
l_ministry1 = ["silly", "walks"]
l_ministry2 = ["walks", "silly"]
l_ministry1 == l_ministry2
# Dictionary Comparison
d_ministry1 = {"a": "silly", "b": "walks"}
d_ministry2 = {"b": "walks", "a": "silly"}
d_ministry1 == d_ministry2

# The keys and values of the dictionary can be called using the `keys()` and `values()` methods. The key/value pairs can
# also be returned with the `items()` method. These three methods return the respective output in list-like fashion.
# This allows the dictionary to be used efficiently in loops.
print(menu.keys())
print(menu.values())
print(menu.items())
for k in menu.keys():
    print(k)
for v in menu.values():
    print(v)
for i in menu.items():
    print(i)

# A dictionary can be sorted by using the `keys()` or `values()` method and converting the output to a list. This list
# can be sorted and displayed for the user.
ordered_keys = list(menu.keys())
print(ordered_keys)
ordered_keys.sort(reverse=True)
print(ordered_keys)

# By using the `tuple()` function, a dictionary can be converted into a tuple. Each item in the tuple will be a tuple as
# well. This is how python handles the key/value pairs in a format that does not technically support that functionality.
# Since this key/value pair is a tuple, slicing can be applied to the sliced item to obtain the key or value.
# Additionally, slicing can be applied to the sliced value, from the sliced tuple, to obtain a specific item in the
# list.
menu_tuple = tuple(menu.items())
print(menu_tuple)
print(type(menu_tuple))
print(menu_tuple[0])
print(type(menu_tuple[0]))
# Slicing the key/value tuple to obtain the key.
print(menu_tuple[0][0])
print(type(menu_tuple[0][0]))
# Slicing the key/value tuple to obtain the value.
print(menu_tuple[0][1])
print(type(menu_tuple[0][1]))
# Slicing the second item in the value list.
print(menu_tuple[0][1][1])
print(type(menu_tuple[0][1][1]))

# Instead of implementing triple slicing to get some spam, let's use the dictionary to obtain the same result.
print(menu["item1"][1])
print(menu_tuple[0][1][1] == menu["item1"][1])

# The `get()` method is a way to retrieve a value from a key, but also contain a default value if no key is found.
order = "item6"
if menu.get(order, 0) == 0:
    print("{} is not a valid dish. Please try again.".format(order))
else:
    print("{} contains {}".format(order, menu.get(order)))

# The `setdefault()` method is used to create a default key/value combination for a dictionary. This is useful for
# applications where verbose data is required, but all of the information is not available. If the dictionary already
# contains a key by the default's name, the value is not changed by the default.
transportation = {"name": "coconut", "color": "brown"}
print(transportation.items())
transportation.setdefault("received_by", "swallow")
print(transportation.items())
transportation.setdefault("received_by", "found_on_ground")
print(transportation.items())

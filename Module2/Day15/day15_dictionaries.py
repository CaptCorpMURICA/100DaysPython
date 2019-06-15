#dictionaries are extermely efficient, allowing the mapping of values to a specific key.
#declared using {} and seperating the key from the value with :
#in order to call, reference the key using [] 
conversation = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}
print(conversation)
print(conversation["a"])

#dictionaries require the key to be a single item, but the value can be a list of multiple items.
menu = {"item1": ["egg", "spam", "bacon"],
        "item2": ["egg", "sausage", "spam"],
        "item3": ["egg", "spam"],
        "item4": ["egg", "bacon", "spam"],
        "item5": ["egg", "bacon", "sausage", "spam"],
        "item6": ["spam", "bacon", "sausage", "spam"],
        "item7": ["spam", "egg", "spam", "spam", "bacon", "spam"],
        "item8": ["spam", "egg", "sausage", "spam"]}
print(menu["item1"])
print(type(menu["item7"]))

menu["item2"] [2] = "spam"
print(menu["item2"])

# List Comparison
l_ministry1 = ["silly", "walks"]
l_ministry2 = ["walks", "silly"]
l_ministry1 == l_ministry2

# Dictionary Comparison
d_ministry1 = {"a": "silly", "b": "walks"}
d_ministry2 = {"b": "walks", "a": "silly"}
d_ministry1 == d_ministry2

print(menu.keys())
print(menu.values())

ordered_keys = list(menu.keys())
print(ordered_keys)
ordered_keys.sort(reverse=True)
print(ordered_keys)
print("=" * 26)

#a dicitionary can be converted to a tuple, each item will be a tuple
menu_tuple = tuple(menu.items())
print(menu_tuple)
print(type(menu_tuple))
print(menu_tuple[0])
print(type(menu_tuple[0]))

#slicing the key/value tuple to obtain the key
print(menu_tuple[0][0])
print(type(menu_tuple[0][0]))

#slicing the key/value to obtain the value
print(menu_tuple[0][1])
print(type(menu_tuple[0][1]))

#slicing the second item in the value list
print(menu_tuple[0][1][1])
print(type(menu_tuple[0][1][1]))

#instead, use the dictionary to obtain the same result
print(menu["item1"])
print(menu["item1"][1])
print(menu_tuple[0][1][1] == menu["item1"][1])

#the get() method is a way to retrieve a value from a key
order = "item6"
if menu.get(order, 0) == 0:
    print("{} is not a valid dish. Please try again.".format(order))
else:
    print("{} contains {}".format(order, menu.get(order)))

#the setdefault() method is used to create  a default key/value combination for a dictionary
transportation ={"name": "coconut", "color": "brown"}
print(transportation.items())
transportation.setdefault("received_by", "swallow")
print(transportation.items())
transportation.setdefault("received_by", "found_on_ground")
print(transportation.items())
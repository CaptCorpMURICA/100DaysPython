# Day 15: Dictionaries 
**Instructions:** 
1. Open a new python file.
2. Dictionaries are extremely useful objects that allow the user to map values to a specific key. These values can be returned simply by calling the key. This makes dictionaries not only useful, but also efficient. A dictionary is declared by using curly brackets (`{}`) and separating the key from the value with a colon (`:`). In order to call the value, the key is referenced in square brackets (`[]`) appended to the name of the dictionary. _Type and execute:_  
   `conversion = {"a": 1, "b": 2, "c": 3, "d": 4, "e": 5}`  
   `print(conversion)`  
   `print(conversion["a"])`
3. Dictionaries require the key to be a single item, but the value can be a list of multiple items. _Type and execute:_  
   `menu = {"item1": ["egg", "spam", "bacon"],`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"item2": ["egg", "sausage", "spam"],`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"item3": ["egg", "spam"],`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"item4": ["egg", "bacon", "spam"],`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"item5": ["egg", "bacon", "sausage", "spam"],`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"item6": ["spam", "bacon", "sausage", "spam"],`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"item7": ["spam", "egg", "spam", "spam", "bacon", "spam"],`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`"item8": ["spam", "egg", "sausage", "spam"]}`  
   `print(menu["item1"])`  
   `print(type(menu["item7"]`
4. Since the value in the `menu` dictionary is a list, it can be changed in the same methodology as a normal list. By using slicing in conjunction with the key, specific items in the list can be retrieved and modified. _Type and execute:_  
   `menu["item2"][2] = "spam"`  
   `print(menu["item2"])`
5. Lists are ordered collections of content, but dictionaries are not. In a dictionary, the key/value pairs can be added in any order. As long as the key/value pairs match between two dictionaries, python will interpret both to be the same. _Type and execute:_  
   `# List Comparison`  
   `l_ministry1 = ["silly", "walks"]`  
   `l_ministry2 = ["walks", "silly"]`  
   `l_ministry1 == l_ministry2`  
   `# Dictionary Comparison`  
   `d_ministry1 = {"a": "silly", "b": "walks"}`  
   `d_ministry2 = {"b": "walks", "a": "silly"}`  
   `d_ministry1 == d_ministry2`  
6. The keys and values of the dictionary can be called using the `keys()` and `values()` methods. _Type and execute:_  
    `print(menu.keys())`  
    `print(menu.values())`
7. A dictionary can be sorted by using the `keys()` or `values()` method and converting the output to a list. This list can be sorted and displayed for the user. _Type and execute:_  
    `ordered_keys = list(menu.keys())`  
    `print(ordered_keys)`  
    `ordered_keys.sort(reverse=True)`  
    `print(ordered_keys)`
8. By using the `tuple()` function, a dictionary can be converted into a tuple. Each item in the tuple will be a tuple as well. This is how python handles the key/value pairs in a format that does not technically support that functionality. Since this key/value pair is a tuple, slicing can be applied to the sliced item to obtain the key or value. Additionally, slicing can be applied to the sliced value, from the sliced tuple, to obtain a specific item in the list. _Type and execute:_  
    `menu_tuple = tuple(menu.items())`  
    `print(menu_tuple)`  
    `print(type(menu_tuple))`  
    `print(menu_tuple[0])`  
    `print(type(menu_tuple[0]))`  
    `# Slicing the key/value tuple to obtain the key.`  
    `print(menu_tuple[0][0])`  
    `print(type(menu_tuple[0][0]))`  
    `# Slicing the key/value tuple to obtain the value.`  
    `print(menu_tuple[0][1])`  
    `print(type(menu_tuple[0][1]))`  
    `# Slicing the second item in the value list.`  
    `print(menu_tuple[0][1][1])`  
    `print(type(menu_tuple[0][1][1]))`
9. Instead of implementing triple slicing to get some spam, let's use the dictionary to obtain the same result. _Type and execute:_  
    `print(menu["item1"][1])`  
    `print(menu_tuple[0][1][1] == menu["item1"][1])` 
10. Update the [log file](../../log.md) with what you have learned today.

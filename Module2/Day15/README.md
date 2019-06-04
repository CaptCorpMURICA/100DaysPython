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
5. 
6. 
7. 
8. 
9. 
10. 
11. 
12. Update the [log file](../../log.md) with what you have learned today.

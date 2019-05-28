# Day 6: Lists
**Instructions:** 
1. Open a new python file.
2. There are two methods for creating an empty list. _Type and execute:_  
   `list_1 = []`  
   `list_2 = list()`  
   `print("List 1 Type: {}\nList 2 Type: {}".format(type(list_1), type(list_2)))`
3. The `list()` function creates a list where each character is a separate entry. _Type and execute:_  
   `text = "Luggage Combination"`  
   `print(list(text))` 
4.  Variables built off a list are treated as the same object. For instance, if a sort is applied to a variable created from a list, the sort is also applied to the original. _Type and execute:_  
   `numbers = [1, 2, 3, 4, 5]`  
   `numbers_sorted = numbers`  
   `numbers_sorted.sort(reverse=True)`  
   `print("numbers: {}\nnumbers_sorted: {}".format(numbers, numbers_sorted))`
5. In order to create a new version, a function needs to be called on the original list when creating a new one. _Type and execute:_  
   `numbers = [1, 2, 3, 4, 5]`  
   `numbers_sorted = list(numbers)`  
   `numbers_sorted.sort(reverse=True)`  
   `print("numbers: {}\nnumbers_sorted: {}".format(numbers, numbers_sorted))`
6. Lists are easily able to be combined using a simple `+` operator. _Type and execute:_  
   `odd = [1, 3, 5]`  
   `even = [2, 4]`  
   `luggage = odd + even`  
   `print(luggage)`
7. There are also several methods to sort the list. _Type and execute:_  
   `odd = [1, 3, 5]`  
   `even = [2, 4]`  
   `luggage = odd + even`  
   `print("Unsorted list: {}".format(luggage))`  
   `print("Using the sorted() function: {}".format(sorted(luggage)))`  
   `luggage.sort()`  
   `print("Using the .sort() method: {}".format(luggage))`
8. Additional items can be added to a list by using the `.append()` method. _Type and execute:_  
   `lines = []`  
   `lines.append("They told me to comb the desert, so I'm combing the desert")`  
   `lines.append("YOGURT! I hate Yogurt! Even with strawberries!")`  
   `lines.append("We'll meet again in Spaceballs 2: The Quest for More Money.")`  
   `lines`
9. Specific items can be retrieved from a list by using its indices and slicing. We will discuss slicing in more detail on [Day 13](../Module1/Day13). _Type and execute:_  
   `lines[0]`  
   `lines[0:2]`  
   `lines[0:3:2]`  
   `lines[::-1]`
10. Update the [log file](../../log.md) with what you have learned today.

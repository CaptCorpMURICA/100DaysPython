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
4. The `.sort()` method is used to sort a list. _Type and execute:_  
   `luggage = [1, 3, 5, 2, 4]`  
   `luggage.sort()`  
   `luggage`
5. Variables built off a list are treated as the same object. For instance, if a sort is applied to a variable created from a list, the sort is also applied to the original. _Type and execute:_  
   `numbers = [1, 2, 3, 4, 5]`  
   `numbers_sorted = numbers`  
   `numbers_sorted.sort(reverse=True)`  
   `print("numbers: {}\nnumbers_sorted: {}".format(numbers, numbers_sorted))`
6. In order to create a new version, a function needs to be called on the original list when creating a new one. _Type and execute:_  
   `numbers = [1, 2, 3, 4, 5]`  
   `numbers_sorted = list(numbers)`  
   `numbers_sorted.sort(reverse=True)`  
   `print("numbers: {}\nnumbers_sorted: {}".format(numbers, numbers_sorted))`
7. Lists are easily able to be combined using a simple `+` operator. _Type and execute:_  
   `odd = [1, 3, 5]`  
   `even = [2, 4]`  
   `luggage = odd + even`  
   `print(luggage)`
8. Lists can also be combined using the `.extend()` method. _Type and execute:_  
   `luggage = [1, 3, 5]`  
   `even = [2, 4]`  
   `luggage.extend(even)`  
   `luggage`
9. There are also several methods to sort the list. _Type and execute:_  
   `odd = [1, 3, 5]`  
   `even = [2, 4]`  
   `luggage = odd + even`  
   `print("Unsorted list: {}".format(luggage))`  
   `print("Using the sorted() function: {}".format(sorted(luggage)))`  
   `luggage.sort()`  
   `print("Using the .sort() method: {}".format(luggage))`
10. Additional items can be added to a list by using the `.append()` method. _Type and execute:_  
   `lines = []`  
   `lines.append("They told me to comb the desert, so I'm combing the desert")`  
   `lines.append("YOGURT! I hate Yogurt! Even with strawberries!")`  
   `lines.append("We'll meet again in Spaceballs 2: The Quest for More Money.")`  
   `lines`
11. Specific items can be retrieved from a list by using its indices and slicing. We will discuss slicing in more detail on [Day 9](../Module1/Day09). _Type and execute:_  
   `lines[0]`  
   `lines[0:2]`  
   `lines[0:3:2]`  
   `lines[::-1]`
12. The index of a requested item can be obtained using the `.index()` method. _Type and execute:_  
   `luggage = [1, 2, 3, 4, 5]`  
   `luggage.index(2)`
13. The frequency of an item in a list can be obtained by using the `.count()` method. This is case sensitive. _Type and execute:_  
   `quote = list("YOGURT! I hate Yogurt! Even with strawberries!")`  
   `quote.count("r")`
14. The `.insert(index, item)` method can be used to add a new item to the list at a specific position. _Type and execute:_  
   `luggage = [1, 2, 4, 5]`  
   `luggage.insert(2, 3)`  
   `luggage`
15. The `.pop(i)` method can be used to remove and return the final element, or from a specific index `i`. _Type and execute:_  
   `luggage = [1, 2, 3, 3, 4, 5, 6]`  
   `luggage.pop()`  
   `luggage`  
   `luggage.pop(2)`  
   `luggage`
16. The `.remove(i)` method eliminates a specific item (`i`) from the list. _Type and execute:_  
   `rng = list(range(0,10))`  
   `rng.remove(7)`  
   `rng`
17. The `.reverse()` method reverses the order of the items in the list. _Type and execute:_  
   `countdown = [5, 4, 3, 2, 1]`  
   `countdown.reverse()`  
   `countdown`
18. Python can conduct transformations to a list while declaring a new list. _Type and execute:_  
   `sample = list(range(1,13))`  
   `times_12 = [i * 12 for i in sample]`  
   `times_12`
19. A list can be cleared by using the `.clear()` method. _Type and execute:_  
   `luggage.clear()`  
   `luggage`
20. Since lists are mutable, items can be changed. _Type and execute:_  
   `luggage = [2, 2, 3, 4, 5]`  
   `luggage[0] = 1`  
   `luggage`
21. Update the [log file](../../log.md) with what you have learned today.

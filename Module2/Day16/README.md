# Day 16: 
**Instructions:** 
1. Open a new python file.
2. Similar to dictionaries, sets are unordered collections of data. Unlike dictionaries, sets do not contain key/value pairs. A set should be used over a list only if there is no need for the collection to be ordered. Sets are created with curly brackets (`{}`) or with the `set()` function. _Type and execute:_  
   `suspects = {"Verbal", "Keaton", "McManus", "Fenster"}`  
   `investigators = set(["Dave Kujan", "Jack Baer", "Jeff Rabin"])`  
   `print(suspects)`  
   `print(investigators)`
3. Sets are mutable, so items can be added to the collection. _Type and execute:_  
   `suspects.add("Hockney")`  
   `print(suspects)`
4. Sets can be iterated through similar to lists. _Type and execute:_  
   `for person in suspects:`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("{} was brought in for a line up.".format(person))`
5. Two sets can be combined using the `union()` method. _Type and execute:_  
   `numbers1 = set([1, 2, 3, 4, 5])`  
   `numbers2 = set([6, 7, 8, 9, 10])`  
   `print(numbers1.union(numbers2))`
6. The `.intersection()` method is used to return only the items that matched between two sets. _Type and execute:_  
   `evens = set([0, 2, 4, 6, 8])`  
   `nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])`  
   `print(nums.intersection(evens))`
7. The `.difference()` method is used to return only the items that don't match between two sets. _Type and execute:_  
   `evens = set([0, 2, 4, 6, 8])`  
   `nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])`  
   `print(nums.difference(evens))`
8. The `.difference_update()` method is used to update a set by removing items that match another set. The method does not produce an output, but overwrites the primary set instead. _Type and execute:_  
   `evens = set([0, 2, 4, 6, 8])`  
   `nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])`  
   `print("Evens: {}".format(nums))`  
   `print("Evens Difference Update: {}".format(nums.difference_update(evens)))`  
   `print("Evens: {}".format(nums))`
9. The `.symmetric_difference()` method can be used to return only the unique items in two sets. _Type and execute:_  
   `evens = set([0, 2, 4, 6, 8])`  
   `nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])`  
   `print(nums.symmetric_difference(evens))`
10. The `.symmetric_difference_update()` method is used to update a set with only the unique items from two sets. The method does not produce an output, but overwrites the primary set instead. _Type and execute:_  
   `evens = set([0, 2, 4, 6, 8])`  
   `nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])`  
   `print("Evens: {}".format(nums))`  
   `print("Symmetric Difference Update: {}".format(nums.symmetric_difference_update(evens)))`  
   `print("Evens: {}".format(nums))`
11. Since sets are unsorted, the `sorted()` function can be used to provide a sorted output. _Type and execute:_  
   `print(suspects)`  
   `print(sorted(suspects))`
12. The `.discard()` and `.remove()` methods are used to remove the specified item from the set. If the specified item is not in the set, the `.remove()` method will throw an error, while the `.discard()` method will not. _Type and execute:_  
   `evens = set([0, 2, 4, 6, 8])`  
   `evens.discard(0)`  
   `evens.remove(2)`  
   `print(evens)`  
   `evens.discard(0)`  
   `evens.remove(2)`  
   `print(evens)`
13. In order to avoid the error while using the `.remove()` error, the `try`/`except` process should be used. _Type and execute:_  
   `suspects = {"Verbal", "Keaton", "McManus", "Fenster"}`  
   `try:`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`suspects.remove("Kaiser Soze")`  
   `except KeyError:`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("Kaiser Soze is not one of the usual suspects.")`
14. While sets are mutable, the `frozenset()` function can be used to create immutable sets. None of the update methods will execute on a `frozenset()`. _Type and execute:_  
   `suspects = frozenset(["Verbal", "Keaton", "McManus", "Fenster"])`  
   `suspects.add("Kaiser Soze")`  
   `print(suspects)`
15. The `.clear()` method empties the entire set. _Type and execute:_  
   `print(nums)`  
   `nums.clear()`  
   `print(nums)`
16. For additional information about [sets](https://www.geeksforgeeks.org/sets-in-python/), read this article. 
17. Update the [log file](../../log.md) with what you have learned today.

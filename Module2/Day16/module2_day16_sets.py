"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module2_day16_sets.py
    Creation Date:  6/5/2019, 10:30 AM
    Description:    Learn about the basics of sets in python.
"""
# Similar to dictionaries, sets are unordered collections of data. Unlike dictionaries, sets do not contain key/value
# pairs. A set should be used over a list only if there is no need for the collection to be ordered. Sets are created
# with curly brackets (`{}`) or with the `set()` function.  Sets are best used for applications that contain a
# collection of stop words. The program is able to scan the contents of a set substantially faster than the contents of
# a list.
suspects = {"Verbal", "Keaton", "McManus", "Fenster"}
investigators = set(["Dave Kujan", "Jack Baer", "Jeff Rabin"])
print(suspects)
print(investigators)

# Sets are mutable, so items can be added to the collection.
suspects.add("Hockney")
print(suspects)

# Sets can be iterated through similar to lists.
for person in suspects:
    print("{} was brought in for a line up.".format(person))

# Two sets can be combined using the `union()` method.
numbers1 = set([1, 2, 3, 4, 5])
numbers2 = set([6, 7, 8, 9, 10])
print(numbers1.union(numbers2))

# The `.intersection()` method is used to return only the items that matched between two sets.
evens = set([0, 2, 4, 6, 8])
nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(nums.intersection(evens))

# The `.difference()` method is used to return only the items that don't match between two sets.
evens = set([0, 2, 4, 6, 8])
nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(nums.difference(evens))

# The `.difference_update()` method is used to update a set by removing items that match another set. The method does
# not produce an output, but overwrites the primary set instead.
evens = set([0, 2, 4, 6, 8])
nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Evens: {}".format(nums))
print("Evens Difference Update: {}".format(nums.difference_update(evens)))
print("Evens: {}".format(nums))

# The `.symmetric_difference()` method can be used to return only the unique items in two sets.
evens = set([0, 2, 4, 6, 8])
nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(nums.symmetric_difference(evens))

# The `.symmetric_difference_update()` method is used to update a set with only the unique items from two sets. The
# method does not produce an output, but overwrites the primary set instead.
evens = set([0, 2, 4, 6, 8])
nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Evens: {}".format(nums))
print("Symmetric Difference Update: {}".format(nums.symmetric_difference_update(evens)))
print("Evens: {}".format(nums))

# Since sets are unsorted, the `sorted()` function can be used to provide a sorted output.
print(suspects)
print(sorted(suspects))

# The `.discard()` and `.remove()` methods are used to remove the specified item from the set. If the specified item is
# not in the set, the `.remove()` method will throw an error, while the `.discard()` method will not.
evens = set([0, 2, 4, 6, 8])
evens.discard(0)
evens.remove(2)
print(evens)
evens.discard(0)
evens.remove(2)
print(evens)

# In order to avoid the error while using the `.remove()` error, the `try`/`except` process should be used.
suspects = {"Verbal", "Keaton", "McManus", "Fenster"}
try:
    suspects.remove("Kaiser Soze")
except KeyError:
    print("Kaiser Soze is not one of the usual suspects.")

# While sets are mutable, the `frozenset()` function can be used to create immutable sets. None of the update methods
# will execute on a `frozenset()`.
suspects = frozenset(["Verbal", "Keaton", "McManus", "Fenster"])
suspects.add("Kaiser Soze")
print(suspects)

# The `.clear()` method empties the entire set.
print(nums)
nums.clear()
print(nums)

#sets are unordered collections of data, and should be used when a substantially faster scan of contents is needed
suspects = {"Verbal", "Keaton", "McManus", "Fenster"}
invesigators = set(["Dave Kujan", "Jack Baar", "Jeff Rabin"])
print(suspects)
print(invesigators)

#items can be added to sets
suspects.add("Hockney")
print(suspects)

for person in suspects:
    print("{} was brought in for a line up.".format(person))

#two sets can be combined using the union() method
numbers1 = set([1, 2, 3, 4, 5])
numbers2 = set([6, 7, 8, 9, 10])
print(numbers1.union(numbers2))

#the intersection() method is used to return only the items matched
evens = set([0, 2, 4, 6, 8])
nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(nums.intersection(evens))

#the difference() method is used to return only the items not matched
evens = set([0, 2, 4, 6, 8])
nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(nums.difference(evens))

#the difference_update() method is used to update a set by removing items that match another set
#doesn't produce an output, but overwrites the primary set
evens = set([0, 2, 4, 6, 8])
nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Evens: {}".format(nums))
print("Evens Difference Update: {}".format(nums.difference_update(evens)))
print("Evans: {}".format(nums))

#the symmetric_difference() method is used to return only the unique items in two sets
evens = set([0, 2, 4, 6, 8])
nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(nums.symmetric_difference(evens))

#the symmetric_difference_update() method updates a set with only the unique items
#similar to the difference_update, it doesn't produce a result, but will overwrite the primary set
evens = set([0, 2, 4, 6, 8])
nums = set([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print("Evens: {}".format(nums))
print("Symmetric Difference Update: {}".format(nums.symmetric_difference_update(evens)))
print("Evens: {}".format(nums))

print(suspects)
print(sorted(suspects))

#discard() and remove() methods are used to remove the specified item
#if the specified item is not in the set, remove() will throw an error
evens = set([0, 2, 4, 6, 8])
evens.discard(0)
evens.remove(2)
print(evens)
evens.discard(0)
# evens.remove(2)
print(evens)

#to avoid the error, the try/ except process should be used
suspects = {"Verbal", "Keaton", "McManus", "Fenster"}
try:
    suspects.remove("Kaiser Soze")
except KeyError:
    print("Kaiser Soze  is not one the usual suspects.")

#the frozenset() function will make the set immutable
suspects = frozenset(["Verbal", "Keaton", "McManus", "Fenster"])
# suspects.add("Kaiser Soze")
print(suspects)

#the clear() method empties the entire set
print(nums)
nums.clear()
print(nums)
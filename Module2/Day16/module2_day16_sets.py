"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module2_day16_sets.py
    Creation Date:  6/5/2019, 10:30 AM
    Description:    Learn about the basics of sets in python.
"""

# Similar to dictionaries, sets are unordered collections of data. Unlike dictionaries, sets do not contain key/value
# pairs. A set should be used over a list only if there is no need for the collection to be ordered. Sets are created
# with curly brackets (`{}`) or with the `set()` function.
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

# Unlike dictionaries, sets can be created empty.
keyser = set()
print(keyser)
keyser.add("Soze")
print(keyser)

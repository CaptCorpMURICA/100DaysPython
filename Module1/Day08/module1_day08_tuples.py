"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module1_day08_tuples.py
    Creation Date:  6/2/2019, 8:55 AM
    Description:    Learn the basics of tuples in python.
"""

# Tuples are different than lists. Lists are mutable, but tuples are immutable. Mutable objects can be changed, but
# immutable objects are static. This makes tuples ideal for items that are not meant to be changed (e.g. movie details).
# Tuples can be created in two main methods. Tuples can be created through a comma separated list of items alone or a
# list of comma separated list of items in parentheses.
theme = "East", "Bound", "Down"
type(theme)
print(theme)
good = ("Bandit", "Frog", "Snowman")
type(good)
print(good)
# Since tuples are immutable, they cannot be changed in the same method as lists.
theme[0] = "West"
# In order to change an item in a tuple, a new tuple needs to be created.
return_trip = "West", theme[1], theme[2]
print(return_trip)
# A tuple can be used to assign multiple variables at the same time.
movie = ("Smokey and the Bandit", 1977, "Hal Needham", ("Burt Reynolds", "Sally Field", "Jerry Reed"))
title, year, director, stars = movie
bandit, frog, snowman = stars
print("Title: {}\nYear: {}\nDirector: {}".format(title, year, director))
type(stars)
print("Stars: {}\nBandit: {}\nFrog: {}\nSnowman: {}".format(stars, bandit, frog, snowman))
# While a tuple cannot be changed, a list contained inside a tuple can be modified.
movie_list = ("Smokey and the Bandit", 1977, "Hal Needham", ["Burt Reynolds", "Sally Field", "Jerry Reed"])
title, year, director, cast = movie_list
type(cast)
print(cast)
cast.append("Jackie Gleason")
print(cast)
# A tuple can be deleted through the `del` command. This can be used to delete an entire tuple, but it cannot be used to
# remove an item in a tuple.
del movie_list

"""
    Author:         Ben Carlson
    Project:        100DaysPython
    File:           module1_day08_tuples.py
    Creation Date:  2019-06-06
    Description:    Tuples
"""

theme = "East", "Bound", "Down"
type(theme)
print(theme)
good = ("Bandit", "Frog", "Snowman")
type(good)
print(good)

# theme[0] = "West"

# to change a tuple you must create a new tuple
return_trip = "West", theme[1], theme[2]
print(return_trip)

# multiple variables at the same time
movie = ("Smokey and the Bandit", 1977, "Hal Needham", ("Burt Reynolds","Sally Field", "Jerry Reed"))
title, year, director, stars = movie
bandit, frog, snowman = stars
print("Title: {}\nYear: {}\nDirector: {}".format(title, year, director))
print("Stars: {}\nBandit: {}\nFrog: {}\nSnowman: {}".format(stars, bandit, frog, snowman))

# change a list inside a tuple
movie_list = ("Smokey and the Bandit", 1977, "Hal Needham", ["Burt Reynolds","Sally Field", "Jerry Reed"])
title, year, director, cast = movie_list
type(cast)
print(cast)
cast.append("Jackie Gleason")
print(cast)

# delete an entire tuple
del movie_list
print(movie_list)



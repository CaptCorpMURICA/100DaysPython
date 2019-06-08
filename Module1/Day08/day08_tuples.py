#tuples are immutable, and are ideal for items not meant to be changed
theme = "East", "Bound", "Down"

print(type(theme))
print(theme)

good = ("Bandit", "Frog", "Snowman")

print(type(good))
print(good)

#tuples cannot be changed in the same method as lists
#theme[0] = "West"

#in order to change an item in a tuple, a new tuple needs to be created
return_trip = "West", theme[1], theme[2]

print(return_trip)
print("break")

#a tuple can be used to assign multiple variables at the same time
movie = ("Smoke the Bandit", 1977, "Hal Needham", ("Burt Reynolds", "Sally Field", "Jerry Reed"))
title, year, director, stars = movie
bandit, frog, snowman = stars

print(f"Title: {title}\n Year: {year}\n Director: {director}")
type(stars)
print(f"Stars: {stars}\n Bandit: {bandit}\n Frog: {frog}\n Snowman: {snowman}")

#use a list to make modifications inside of a tuple
movie_list = ("Smoke the Bandit", 1977, "Hal Needham", ["Burt Reynolds", "Sally Field", "Jerry Reed"])
title, year, director, cast = movie_list
type(cast)

print(cast)
cast.append("Jackie Gleason")
print(cast)

#a single item in a tuple cannot be deleted, but an entire tuple can de deleted
del movie_list
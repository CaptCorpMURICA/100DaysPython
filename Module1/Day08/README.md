# Day 8: Tuples
**Instructions:** 
1. Open a new python file.
2. Tuples are different than lists. Lists are mutable, but tuples are immutable. Mutable objects can be changed, but immutable objects are static. This makes tuples ideal for items that are not meant to be changed (e.g. movie details).
3. Tuples can be created in two main methods. Tuples can be created through a comma separated list of items alone or a list of comma separated list of items in parentheses. _Type and Execute:_  
   `theme = "East", "Bound", "Down"`  
   `type(theme)`  
   `print(theme)`  
   `good = ("Bandit", "Frog", "Snowman")`  
   `type(good)`  
   `print(good)`
4. Since tuples are immutable, they cannot be changed in the same method as lists. _Type and execute:_  
   `theme[0] = "West"`
5. In order to change an item in a tuple, a new tuple needs to be created. _Type and execute:_  
   `return_trip = "West", theme[1], theme[2]`  
   `print(return_trip)`
6. A tuple can be used to assign multiple variables at the same time. _Type and execute:_  
   `movie = ("Smokey and the Bandit", 1977, "Hal Needham", ("Burt Reynolds", "Sally Field", "Jerry Reed"))`  
   `title, year, director, stars = movie`  
   `bandit, frog, snowman = stars`  
   `print("Title: {}\nYear: {}\nDirector: {}".format(title, year, director))`  
   `type(stars)`  
   `print("Stars: {}\nBandit: {}\nFrog: {}\nSnowman: {}".format(stars, bandit, frog, snowman))`
7. While a tuple cannot be changed, a list contained inside a tuple can be modified. _Type and execute:_  
   `movie_list = ("Smokey and the Bandit", 1977, "Hal Needham", ["Burt Reynolds", "Sally Field", "Jerry Reed"])`  
   `title, year, director, cast = movie_list`  
   `type(cast)`  
   `print(cast)`  
   `cast.append("Jackie Gleason")`  
   `print(cast)`
8. A tuple can be deleted through the `del` command. This can be used to delete an entire tuple, but it cannot be used to remove an item in a tuple. _Type and execute:_  
   `del movie_list`
9. Update the [log file](../../log.md) with what you have learned today.

"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module2_day25_comprehensions.py
    Creation Date:  6/19/2019, 9:41 AM
    Description:    Learn the basics of list comprehensions in python.
"""

# Create a list of items from 1 to 100 divisible by 7.
sevens = []
for i in range(1, 101):
    if i % 7 == 0:
        sevens.append(i)

print(sevens)

# Similar to lambda functions, list comprehensions are a method of condensing python code into a single line. A list can
# be created with a single line containing the for loop and applicable if statements.
sevens_comprehension = [i for i in range(1, 101) if i % 7 == 0]
print(sevens_comprehension)

# Additional actions can be taken to transform the iterator during this process. By multiplying `i` by two, only the
# multiples of seven are returned, but the values are doubled.
sevens_doubled = [i * 2 for i in range(1, 101) if i % 7 == 0]
print(sevens_doubled)

# List comprehensions can also be used for string functions. By iterating through the list using string manipulations
# and a `for` loop, a list can be generated using conditions that would take 3+ lines of code normally.
winners = ['Green Bay', 'Green Bay', 'New York Jets', 'Kansas City', 'Baltimore', 'Dallas', 'Miami', 'Miami',
           'Pittsburgh', 'Pittsburgh', 'Oakland', 'Dallas', 'Pittsburgh', 'Pittsburgh', 'Oakland', 'San Francisco',
           'Washington', 'Los Angeles Raiders', 'San Francisco', 'Chicago', 'New York Giants', 'Washington',
           'San Francisco', 'San Francisco', 'New York Giants', 'Washington', 'Dallas', 'Dallas', 'San Francisco',
           'Dallas', 'Green Bay', 'Denver', 'Denver', 'St. Louis', 'Baltimore', 'New England', 'Tampa Bay',
           'New England', 'New England', 'Pittsburgh', 'Indianapolis', 'New York Giants', 'Pittsburgh', 'New Orleans',
           'Green Bay', 'New York Giants', 'Baltimore', 'Seattle', 'New England', 'Denver', 'New England',
           'Philadelphia', 'New England']
vowel_winners = [team for team in winners if team.lower()[0] in 'aeiou']
print(vowel_winners)

# List comprehensions can be used against tuples in a list as well. By calling the position in the tuple, filters and
# transformations can be completed on any element within the tuple.
super_bowl = [('Green Bay', 'Kansas City'), ('Green Bay', 'Oakland'), ('New York Jets', 'Baltimore'),
              ('Kansas City', 'Minnesota'), ('Baltimore', 'Dallas'), ('Dallas', 'Miami'), ('Miami', 'Washington'),
              ('Miami', 'Minnesota'), ('Pittsburgh', 'Minnesota'), ('Pittsburgh', 'Dallas'), ('Oakland', 'Minnesota'),
              ('Dallas', 'Denver'), ('Pittsburgh', 'Dallas'), ('Pittsburgh', 'Los Angeles Rams'),
              ('Oakland', 'Philadelphia'), ('San Francisco', 'Cincinnati'), ('Washington', 'Miami'),
              ('Los Angeles Raiders', 'Washington'), ('San Francisco', 'Miami'), ('Chicago', 'New England'),
              ('New York Giants', 'Denver'), ('Washington', 'Denver'), ('San Francisco', 'Cincinnati'),
              ('San Francisco', 'Denver'), ('New York Giants', 'Buffalo'), ('Washington', 'Buffalo'),
              ('Dallas', 'Buffalo'), ('Dallas', 'Buffalo'), ('San Francisco', 'San Diego'), ('Dallas', 'Pittsburgh'),
              ('Green Bay', 'New England'), ('Denver', 'Green Bay'), ('Denver', 'Atlanta'), ('St. Louis', 'Tennessee'),
              ('Baltimore', 'New York Giants'), ('New England', 'St. Louis'), ('Tampa Bay', 'Oakland'),
              ('New England', 'Carolina'), ('New England', 'Philadelphia'), ('Pittsburgh', 'Seattle'),
              ('Indianapolis', 'Chicago'), ('New York Giants', 'New England'), ('Pittsburgh', 'Arizona'),
              ('New Orleans', 'Indianapolis'), ('Green Bay', 'Pittsburgh'), ('New York Giants', 'New England'),
              ('Baltimore', 'San Francisco'), ('Seattle', 'Denver'), ('New England', 'Seattle'), ('Denver', 'Carolina'),
              ('New England', 'Atlanta'), ('Philadelphia', 'New England'), ('New England', 'Los Angeles Rams')]

philly_showings = [winner for (winner, loser) in super_bowl if winner == 'Philadelphia' or loser == 'Philadelphia']
print(philly_showings)


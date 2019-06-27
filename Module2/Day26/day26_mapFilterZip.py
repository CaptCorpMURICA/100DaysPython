#calculate the area based on a list of radii
import math 

def area(r: float) -> float:
    """
    Calculate the area of a circle based on the radius.
    :param r: The radius of the circle: Float
    :return: The area of the circle: Float
    """
    return math.pi * (r ** 2)


radii = [4, 5, 123, 42, 12.5]

areas = []
for rad in radii:
    a = area(rad)
    areas.append(a)

print(areas)

#can be completed in a single line using map() and lambdas
#map() requires two inputs: map(function, iterative object)
#map() creates a map object
import math 
radii = [4, 5, 123, 42, 12.5]
areas = list(map(lambda r: math.pi * (r ** 2), radii)) #list() required to produce the final list output
print(areas)
print(map(lambda r: math.pi * (r ** 2), radii))

#the filter() is similar, but it used to only return items that return True
#the filter() created a filter object
#now, filter all even values out of a list
odds = list(filter(lambda i: i % 2, range(100)))
print(odds)
print(filter(lambda i: i % 2, range(100)))

#the zip() is used to create an iterable object of tuples that joins multiple lists
#the zip()compresses multiple iterable objects into a single object

sb_num = ['I', 'II', 'III', 'IV', 'V', 'VI', 'VII', 'VIII', 'IX', 'X', 'XI', 'XII', 'XIII', 'XIV', 'XV', 'XVI', 'XVII',
          'XVIII', 'XIX', 'XX', 'XXI', 'XXII', 'XXIII', 'XXIV', 'XXV', 'XXVI', 'XXVII', 'XXVIII', 'XXIX', 'XXX', 'XXXI',
          'XXXII', 'XXXIII', 'XXXIV', 'XXXV', 'XXXVI', 'XXXVII', 'XXXVIII', 'XXXIX', 'XL', 'XLI', 'XLII', 'XLIII',
          'XLIV', 'XLV', 'XLVI', 'XLVII', 'XLVIII', 'XLIX', '50', 'LI', 'LII', 'LIII']

sb_date = ['Jan. 15, 1967', 'Jan. 14, 1968', 'Jan. 12, 1969', 'Jan. 11, 1970', 'Jan. 17, 1971', 'Jan. 16, 1972',
           'Jan. 14, 1973', 'Jan. 13, 1974', 'Jan. 12, 1975', 'Jan. 18, 1976', 'Jan. 9, 1977', 'Jan. 15, 1978',
           'Jan. 21, 1979', 'Jan. 20, 1980', 'Jan. 25, 1981', 'Jan. 24, 1982', 'Jan. 30, 1983', 'Jan. 22, 1984',
           'Jan. 20, 1985', 'Jan. 26, 1986', 'Jan. 25, 1987', 'Jan. 31, 1988', 'Jan. 22, 1989', 'Jan. 28, 1990',
           'Jan. 27, 1991', 'Jan. 26, 1992', 'Jan. 31, 1993', 'Jan. 30, 1994', 'Jan. 29, 1995', 'Jan. 28, 1996',
           'Jan. 26, 1997', 'Jan. 25, 1998', 'Jan. 31, 1999', 'Jan. 30, 2000', 'Jan. 28, 2001', 'Feb. 3, 2002',
           'Jan. 26, 2003', 'Feb. 1, 2004', 'Feb. 6, 2005', 'Feb. 5, 2006', 'Feb. 4, 2007', 'Feb. 3, 2008',
           'Feb. 1, 2009', 'Feb. 7, 2010', 'Feb. 6, 2011', 'Feb. 5, 2012', 'Feb. 3, 2013', 'Feb. 2, 2014',
           'Feb. 1, 2015', 'Feb. 7, 2016', 'Feb. 5, 2017', 'Feb. 4, 2018', 'Feb. 3, 2019']

sb_winners = ['Green Bay', 'Green Bay', 'New York Jets', 'Kansas City', 'Baltimore', 'Dallas', 'Miami', 'Miami',
              'Pittsburgh', 'Pittsburgh', 'Oakland', 'Dallas', 'Pittsburgh', 'Pittsburgh', 'Oakland', 'San Francisco',
              'Washington', 'Los Angeles Raiders', 'San Francisco', 'Chicago', 'New York Giants', 'Washington',
              'San Francisco', 'San Francisco', 'New York Giants', 'Washington', 'Dallas', 'Dallas', 'San Francisco',
              'Dallas', 'Green Bay', 'Denver', 'Denver', 'St. Louis', 'Baltimore', 'New England', 'Tampa Bay',
              'New England', 'New England', 'Pittsburgh', 'Indianapolis', 'New York Giants', 'Pittsburgh',
              'New Orleans', 'Green Bay', 'New York Giants', 'Baltimore', 'Seattle', 'New England', 'Denver',
              'New England', 'Philadelphia', 'New England']

sb_losers = ['Kansas City', 'Oakland', 'Baltimore', 'Minnesota', 'Dallas', 'Miami', 'Washington', 'Minnesota',
             'Minnesota', 'Dallas', 'Minnesota', 'Denver', 'Dallas', 'Los Angeles Rams', 'Philadelphia', 'Cincinnati',
             'Miami', 'Washington', 'Miami', 'New England', 'Denver', 'Denver', 'Cincinnati', 'Denver', 'Buffalo',
             'Buffalo', 'Buffalo', 'Buffalo', 'San Diego', 'Pittsburgh', 'New England', 'Green Bay', 'Atlanta',
             'Tennessee', 'New York Giants', 'St. Louis', 'Oakland', 'Carolina', 'Philadelphia', 'Seattle', 'Chicago',
             'New England', 'Arizona', 'Indianapolis', 'Pittsburgh', 'New England', 'San Francisco', 'Denver',
             'Seattle', 'Carolina', 'Atlanta', 'New England', 'Los Angeles Rams']

sb_score = [(35, 10), (33, 14), (16, 7), (23, 7), (16, 13), (24, 3), (14, 7), (24, 7), (16, 6), (21, 17), (32, 14),
            (27, 10), (35, 31), (31, 19), (27, 10), (26, 21), (27, 17), (38, 9), (38, 16), (46, 10), (39, 20), (42, 10),
            (20, 16), (55, 10), (20, 19), (37, 24), (52, 17), (30, 13), (49, 26), (27, 17), (35, 21), (31, 24),
            (34, 19), (23, 16), (34, 7), (20, 17), (48, 21), (32, 29), (24, 21), (21, 10), (29, 17), (17, 14), (27, 23),
            (31, 17), (31, 25), (21, 17), (34, 31), (43, 8), (28, 24), (24, 10), (34, 28), (41, 33), (13, 3)]

super_bowl = list(zip(sb_num, sb_date, sb_winners, sb_losers, sb_score))
print(super_bowl)

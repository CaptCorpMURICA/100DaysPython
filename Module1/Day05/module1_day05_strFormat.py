"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module1_day05_strFormat.py
    Creation Date:  6/2/2019, 8:55 AM
    Description:    Learn the basics of formatting strings in python.
"""

# Python contains built in methods to modify strings.
cheers = "where everybody knows YOUR name."
# Applies proper casing to the string.
cheers.capitalize()
# Applies proper casing for use in titles.
cheers.title()
# Converts the entire string into lowercase.
cheers.lower()
# Converts the entire string into uppercase.
cheers.upper()
# Inverts the casing on the string. If it was lowercase, it would be turned uppercase and vice versa.
cheers.swapcase()
# These methods do not have to be applied only to variables. They can also be applied directly to strings or other
# objects.
"norm".upper()

# As briefly mentioned in previous days, python uses string replacement to easily add information to a print statement.
# This method can be used to ignore type errors in concatenation between strings and numbers.
spinoff = "Frasier"
yr = 1993
print("The show {} was a spinoff of Cheers that first aired in {}.".format(spinoff, yr))
# The precision and format of the replacement can also be altered within in the print statement by using `{}`.
# This functionality uses the format of `{Position:Width}`.
i = 13
print("{0:2} squared is {1:4}.".format(i, i ** 2))
# Within the formatting declaration, `<` can be used for left justification, `>` can be used for right justification,
# and `^` can be used for center justification.
i = 13
print("{0:2} squared is {1:<4}.".format(i, i ** 2))
print("{0:2} squared is {1:>4}.".format(i, i ** 2))
print("{0:2} squared is {1:^4}.".format(i, i ** 2))
# Additional characters can be added to the padding as part of the format statement by adding the character after the
# colon.
msg = "END OF CODE"
print("{:=^50}".format(msg))
# Long strings can be truncated by using a number after a period.
print("{:.5}".format(cheers.capitalize()))
# Numbers can also be formatted to produce specific results.
pi = 22 / 7
print("Pi as a float is {0:f}, as a float with a precision of 2 is {0:.2f}.".format(pi))
print("The answer to life, the universe, and everything is {0:d} as an integer, or {0:=^10d} as a padded and centered "
      "integer.".format(42))
# For additional examples, review the [PyFormat](https://pyformat.info/) documentation.
# These same methodologies can be used with [f-strings]
# (https://docs.python.org/3/reference/lexical_analysis.html#f-strings).
pi = 22 / 7
print(f"Pi as a float is {pi:f}, as a float with a precision of 2 is {pi:.2f}")
print(f"The answer to life, the universe, and everything is {42:d} as an integer, or {42:=^10d} as a padded and "
      f"centered integer.")

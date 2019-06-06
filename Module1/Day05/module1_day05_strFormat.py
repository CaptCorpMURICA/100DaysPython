"""
    Author:         Ben Carlson
    Project:        100DaysPython
    File:           module1_day05_strFormat.py
    Creation Date:  2019-06-04
    Description:    String Formatting
"""

# Built in methods to modify strings
cheers = "where everybody knows YOUR name."
cheers.capitalize()  # Applies proper casing to the string.
cheers.title()  # Applies proper casing for use in titles.
cheers.lower()  # Converts the entire string into lowercase.
cheers.upper()  # Converts the entire string into uppercase.
cheers.swapcase()  # Inverts the casing on the string. If it was lowercase, it would be turned uppercase and vice versa.
"norm".upper()  # These methods do not have to be applied only to variables.
# They can also be applied directly to strings or other objects.

spinoff = "Frasier"
yr = 1993
print("The show {} was a spinoff of Cheers that first aired in {}".format(spinoff, yr))

i = 13
print("{0:2} squared is {1:4}.".format(i, i ** 2))
print("{0:2} squared is {1:<4}.".format(i, i ** 2))
print("{0:2} squared is {1:>4}.".format(i, i ** 2))
print("{0:2} squared is {1:^4}.".format(i, i ** 2))

msg = "END OF CODE"
print("{:=^50}".format(msg))

print("{:.5}".format(cheers.capitalize()))

pi = 22 / 7
print("Pi as a float is {0:f}, as a float with a precision of 2 is {0:.2f}".format(pi))

print(f"Pi as a float is {pi:f}, as a float with a precision of 2 is {pi:.2f}")

print(f"The answer to life, the universe, and everything is {42:d} as an integer, or {42:=^10d} as padded and centered integer")

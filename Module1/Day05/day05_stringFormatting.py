#modify strings
cheers = "where everybody knows YOUR name."
cheers.capitalize() # Applies proper casing to the string. 
cheers.title() # Applies proper casing to the string.
cheers.lower() # Converts the entire string into lowercase.
cheers.upper() # Converts the entire string into uppercase.
cheers.swapcase() # Inverts the casing to the string. If it was lowercase, it would be turned uppercase and vice versa.
"norm".upper() # These methods do not have to be applied only to the variable. They can also be applied directly to strings or other objects. 

#string replacement to easily add information to a print statement
spinoff = "Frasier"
yr = 1993

print("The show {} was a spinoff of Cheers that first aired in {}".format(spinoff,yr))
print(f"The show {spinoff} was a spinoff of Cheers that first aired in {yr}")

#the precision and format of the replacement can also be altered
i = 13 

print("{0:2} squared is {1:4}.".format(i, i ** 2))
print("{0:2} squared is {1:<4}.".format(i, i ** 2))
print("{0:2} squared is {1:>4}.".format(i, i ** 2))
print("{0:2} squared is {1:^4}.".format(i, i ** 2))

#additional characters can be added to the padding
msg = "END OF CODE"
print("{:.5}".format(msg))

#long strings can be truncated 
print("{:.5}".format(cheers.capitalize()))

#numbers can also be formatted to produce specific results
pi = 22 / 7
print("Pi as a float is {0:f}, as a float with a precision of 2 is {0:.2f}".format(pi))
print("The answer to life, the universe, and everything is {0:d} as an integer, or {0:=^10d} as a padded and centered integer".format(42))

#now use a f-string
pi= 22 / 7
print(f"Pi as a float is {pi:f}, as a float with a precision of 2 is {pi:.2f}")
# Day 5:  String Formatting
**Instructions:** 
1. Open a new python file.
2. Python contains built in methods to modify strings. _Type and execute:_  
   `cheers = "where everybody knows YOUR name."`  
   `cheers.capitalize() # Applies proper casing to the string.`  
   `cheers.title() # Applies proper casing for use in titles.`  
   `cheers.lower() # Converts the entire string into lowercase.`  
   `cheers.upper() # Converts the entire string into uppercase.`  
   `cheers.swapcase() # Inverts the casing on the string. If it was lowercase, it would be turned uppercase and vice versa.`  
   `"norm".upper() # These methods do not have to be applied only to variables. They can also be applied directly to strings or other objects.`
3. As briefly mentioned in previous days, python uses _string replacement_ to easily add information to a print statement. This method can be used to ignore type errors in concatenation between strings and numbers. _Type and execute:_  
   `spinoff = "Frasier"`  
   `yr = 1993`  
   `print("The show {} was a spinoff of Cheers that first aired in {}".format(spinoff, yr))`
4. The precision and format of the replacement can also be altered within in the print statement by using `{}`. This functionality uses the format of `{Position:Width}`. _Type and execute:_  
   `i = 13`  
   `print("{0:2} squared is {1:4}.".format(i, i ** 2))`
5. Within the formatting declaration, `<` can be used for left justification, `>` can be used for right justification, and `^` can be used for center justification. _Type and execute:_  
   `i = 13`  
   `print("{0:2} squared is {1:<4}.".format(i, i ** 2))`  
   `print("{0:2} squared is {1:>4}.".format(i, i ** 2))`  
   `print("{0:2} squared is {1:^4}.".format(i, i ** 2))`
6. Additional characters can be added to the padding as part of the format statement by adding the character after the colon. _Type and execute:_  
   `msg = "END OF CODE"`  
   `print("{:=^50}".format(msg))`
7. Long strings can be truncated by using a number after a period. _Type and execute:_
   `print("{:.5}".format(cheers.capitalize()))`  
8. Numbers can also be formatted to produce specific results. _Type and execute:_  
   `pi = 22 / 7`  
   `print("Pi as a float is {0:f}, as a float with a precision of 2 is {0:.2f}".format(pi))`  
   `print("The answer to life, the universe, and everything is {0:d} as an integer, or {0:=^10d} as a padded and centered integer".format(42))`
9. For additional examples, review the [PyFormat](https://pyformat.info/) documentation. Update the [log file](../../log.md) with what you have learned today.

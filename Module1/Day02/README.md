# Day 2: Printing in Python
**Instructions:** 
1. Open a new python file.
2. The print statement can be used to display strings.  
   `print("Hello World")`
3. You can also concatenate strings within a print statement.  
   `print("Hello" + " " + "World")`
4. By using multiplication, you can repeat a string a specific number of times.  
   `print("Rudy " * 5)`
5. You can also add newlines and tabs into your print statement.  
   `print("Ew\n\tWhat do you mean 'Ew'? I don't like spam.")`
6. Print statements aren't just for strings. You can also complete arithmetic operations.  
   `print(1 + 1)`
7. But can you combine strings and integers in the same print statement?  
   `print("This is the answer to life, the universe, and everything: " + 42)`
8. Now try this instead.  
   `print("This is the answer to life, the universe, and everything: " + str(42))`
9. This is how you implement [string replacement formatting](https://pyformat.info/). As you can see, by using this method, you do not need to convert integers into strings in order to add it to this print statement. _Type and execute_  
   `print("The number of the {} shall be {}. No more. No less".format("counting", 3))`
10. Instead of using string replacement formatting, you can also use formatted string literals (or [f-strings](https://docs.python.org/3/refernce/lexical_analysis.html#f-strings) for short).  
   `print(f"The number of the {'counting'} shall be {3}. No more. No less")`
11. The replacements can also be done using integer locations. **_As a note:_** Python starts counting at 0. The integers provide the location within the format() method in which to use for replacement.  
   `print("The number of the {1} shall be {0}. No more. No less".format(3, "counting"))`
12. Update the [log file](../../log.md) with what you have learned today.

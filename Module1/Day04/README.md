# Day 4: Variables & Variable Types
**Instructions:** 
1. Open a new python file.
2. Variables need to start with a letter or an underscore. Numbers can be used in the variable name as long as it is not the first character. Additionally, python is case sensitive, so the same word can store multiple items as long as the casing differs. _Type and execute:_  
   `greeting = "Hello"`  
   `_name = "General Kenobi."`  
   `Greeting = "There"`  
   `_bestLine_ep3_ = "You are a bold one."`  
   _Using string concatenation:_ `print(greeting + " " + Greeting + "\n\t" + _name + " " + _bestLine_ep3_)`  
   _Using string replacement:_ `print("{} {}\n\t{} {}".format(greeting, Greeting, _name, _bestLine_ep3_))`
3. Variables can also store numeric values. _Type and execute:_  
   `released = 2005`  
   _Using string concatenation:_ `print("Revenge of the Sith was released on May 4, " + str(released) + ".")`  
   _Using string replacement:_ `print("Revenge of the Sith was released on May 4, {}.".format(released))`
4. Variables are commonly used in arithmetic operations. _Type and execute:_  
   `a = 3`  
   `b = 4`  
   `c = a ** 2 + b ** 2`  
   `print("Pythagorean Theorem: a^2 + b^2 = c^2, so when a = {} and b = {}, then c = {}".format(a, b, c))`
5. You can test for contents in a variable. If the test results **True**, then the tested condition is in the variable. Otherwise, the test returns **False**.  _Type and execute:_  
   `film = "Revenge of the Sith"`  
   `print("Sith" in film)`  
   `print("sith" in film)`  
   `print("sith" in film.lower())`
6. Python variables get their type with the data that is stored. Unlike other programming languages, you do not declare a type for the variable. Additionally, the same variable can be overwritten with new data and a different type. This should be taken into account when creating python programs. _Type and execute:_  
   `var = "Variables are mutable"`  
   `type(var)`  
   `var = 3`  
   `type(var)`  
   `var = 3.5`  
   `type(var)`  
   `var = int(var) # If the variable contains a numeric value, it can be converted to an integer type with the int() function.`  
   `type(var)`  
   `var = str(var) # The variable can be converted to a string with the str() function regardless of the contents.`  
   `type(var)`  
   `var = float(var) # If the variable contains a numeric value, it can be converted to an float type with the float() function.`  
   `type(var)`    
   `var = True`  
   `type(var)`
7. Update the [log file](../../log.md) with what you have learned today.

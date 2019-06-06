#variables start with either a letter or an underscore
greeting = "Hello"
_name = "General Kenobi."
Greeting = "There"
_bestLine_ep3_ = "You are a bold one."

print(greeting + " " + Greeting + "\n\t" + _name + " " + _bestLine_ep3_)
print("{} {}\n\t{} {}".format(greeting,Greeting,_name,_bestLine_ep3_))
print(f"{greeting} {Greeting} \n\t {_name} {_bestLine_ep3_}")

#variables can also store numeric values
released = 2005 

print("Revenge of the Sith was released on May 4, " + str(released) + ".")
print("Revenge of the Sith was released on May 4, {}.".format(released))
print(f"Revenge of the Sith was released on May 4, {released}.")

#variables are commonly used in arithmetic operations 
a = 3 
b = 4
c = a ** 2 + b ** 2

print("Pythagorean Theorem: a^2 + b^2 = c^2, so when a = {} and b = {}, then c = {}".format(a,b,c))
print(f"Pythagorean Theorem: a^2 + b^2 = c^2, so when a = {a} and b = {b}, then c = {c}")

#test for contents in a variable
film = "Revenge of the Sith"
print("Sith" in film)
print("sith" in film)
print("sith" in film.lower())

#python variables get their type with the data that is stored
var = "Variables are mutable"
type(var)
var = 3
type(var)
var = 3.5
type(var)
var = int(var) # If the variable contains a numeric value, it can be converted to an integer type with the int() function.
type(var)
var = str(var) # The variable can be converted to a string with the str() function regardless of the contents.
type(var)
var = float(var) # IF the variable contains a numeric value, it can be converted to a float type with the float() function.
type(var)
var = True
print(type(var))
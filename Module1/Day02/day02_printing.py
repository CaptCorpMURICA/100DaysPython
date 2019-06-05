#the print statment
print("Hello World")

#concantenate strings
print("Hello" + " " + "World")

#repeate strings
print("Rudy" *5)

#add newlines and tabs
print("Ew\n\tWhat do you mean 'Ew'? \n\tI don't like spam.")

#complete arithmetic operations
print(1 + 1)

#can't combine strings and integers 
#print("This is the answer to life, the universe, and everything:" + 42)

#need to specify data types when combining two distinct types
print("This is the answer to life, the universe, and everything:" + str(42))

#or, use string replacement formatting
print("The number of the {} shall be {}. No more. No less".format("counting", 3))

#or, use f-strings which are less verbose and can work with all valid python expressions
print(f"The number of the {'counting'} shall be {3}. No more. No less")

name = "Julian"
age = 28
print(f"Hello, {name}. You are {age}.")
print(f"{name.lower()} is smart")

last_name = "Chavez"
profession = "analyst"
company = "comcast"
message = (
    f"Hi Julian {last_name}. "
    f"You are an {profession}. "
    f"You work for {company}. "
)
print(message)

#replacements can also be done using integer locations
print("The number of the {1} shall be {0}. No more. No less".format(3, "counting"))

print(f"The number of the {'counting'} shall be {3}. No more. No less")
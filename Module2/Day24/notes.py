#Decorators 
#first, quick review of closures
#first class functions allows us to treat functions like any other object


def outer_function():
    message = 'Hi'

    def inner_function():
        print(message) #the inner function has access to the message variable, making it a free variable
    return inner_function()

outer_function()


#closures allow us to take advantage of first class functions 


def outer_function():
    message = 'Hi'

    def inner_function():
        print(message) 
    return inner_function #instead of executing the inner function and returning it, lets instead return the function without returning it

#outer_function() #when this is executed it returns the inner function waiting to be executed
my_func = outer_function()
my_func()
my_func()
print("=" * 26)

#now let's pass in a few more arguments 


def outer_function(msg):
    message = msg

    def inner_function():
        print(message) 
    return inner_function 

hi_func = outer_function('Hi') #now that the outer function takes in some arguments, now you can create two different variables
bye_func = outer_function('Bye')

hi_func()
bye_func()


#another way of writing it...


def outer_function(msg): #the message variable is only getting the value of the msg argument
    def inner_function():
        print(msg) 
    return inner_function 

hi_func = outer_function('Hi') 
bye_func = outer_function('Bye')

hi_func()
bye_func()
print("=" * 26)


# a decorator is a function that takes another function as an argument
# adds some kind of functionality
# returns another function. without altering the source code of the original function passed in



def decorator_function(original_function):
    def wrapper_function():
        return original_function
    return wrapper_function #returns the wrapper waiting to be executed


def display():
    print('display function ran')

decorated_display = decorator_function(display) #this variable passes in our display function to our decorator function 

decorated_display()
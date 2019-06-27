# a decorator is a function that takes another function as an argument, adds some kind of functionality, andreturns another function. without altering the source code of the original function passed in


def decorator_function(original_function):
    def wrapper_function():
        return original_function()
    return wrapper_function 


def display():
    print('display function ran')

decorated_display = decorator_function(display) #passed in the display function which is equal to original function in the wrapper function

decorated_display()


#what are the benefits to doing this? you can make changes to the wrapper function for added functionality


def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__)) #pass in name of the original function
        return original_function()
    return wrapper_function 


def display():
    print('display function ran')

decorated_display = decorator_function(display) #passed in the display function which is equal to original function in the wrapper function

decorated_display()
print("=" * 26)

#but it can be written in an easier way


def decorator_function(original_function):
    def wrapper_function():
        print('wrapper executed this before {}'.format(original_function.__name__)) #pass in name of the original function
        return original_function()
    return wrapper_function 


@decorator_function
def display():
    print('display function ran')

display()
print("=" * 26)


#if you want the original function to take in arguments, you need to do pass in positional or keyword arguments into the wrapper and have it execute the original function 


def decorator_function(original_function):
    def wrapper_function(*args, **kwargs):
        print('wrapper executed this before {}'.format(original_function.__name__))
        return original_function(*args, **kwargs) #need to be passed into the original function
    return wrapper_function 


@decorator_function
def display():
    print('display function ran')

@decorator_function
def display_info(name, age):
    print('display_info ran with arguments ({}, {})'.format(name, age))

display_info('Julian', 28)

display()
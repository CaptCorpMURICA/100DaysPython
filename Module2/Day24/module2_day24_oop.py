"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module2_day24_oop.py
    Creation Date:  6/16/2019, 8:54 AM
    Description:    Learn the foundation of object-oriented programming with python.
"""

# A decorator is a function that leverages another function without changing it. This Primer on Python Decorators]
# provides a good overview of this key functionality and how it can be harnessed with real world examples.


def bar():
    print("This is the bar()")


def foo(f):
    print("This is the foo()")
    f()
    print("This is the function name: {}".format(f.__name__))


foo(bar)

# The "pie" syntax (`@`) is an easier method of using decorators. The "pie" syntax can be used to declare the function
# being called as the declarator, followed by the function used as an input to the declarator. This changes the required
# order of the functions; the declarator functions need to be executed before the "pie" syntax command. If the "pie"
# syntax is called before the `foo()` function is declared, the program will throw an error. Similar to the lambda
# function, the "pie" syntax is an effective method for eliminating extraneous code, but it can reduce the overall
# readability of the program.


def foo(f):
    print("This is the foo()")
    f()
    print("This is the function name: {}".format(f.__name__))


@foo
def bar():
    print("This is the bar()")


# Decorator functions can be written to accept positional (`*args`) and keyword (`**kargs`) arguments.
import time


def waiting(t=0.5):
    """
    Function to sleep the program for time `t` with default of 0.5 seconds.
    :param t: Number of seconds for the program to wait.
    :return: Causes the program to wait and does not return an output.
    """
    time.sleep(t)


def program_time(f):
    """
    Calculates the program time by using decoration and the sleep function.
    :param f: function
    :return: Output of internal calc_time function
    """
    def calc_time(*args, **kwargs):
        """
        Internal function to call the decoration function and calculate program time.
        :param args: Can accept positional arguments to call the decoration function.
        :param kwargs: Can accept keyword arguments to call the decoration function.
        :return: Prints the time taken with embedded wait from the decoration function.
        """
        t = time.time()
        f(*args, **kwargs)
        print("{}() took {} to complete.".format(f.__name__, time.time() - t))
    return calc_time


# Decorator declaration
f = program_time(waiting)

f()  # Calls the function with the default value as the waiting argument
f(1)  # Calls the function with the waiting argument set as 1 second
f(t=5)  # Calls the function with the waiting argument set as 5 seconds
print("Output of calling __name__ on decorator `f`: {}. This differs from the __name__ of the function when it is "
      "called in the calc_time() function.".format(f.__name__))

# There can be high levels of complexity added to applications through the use of multiple decorators. While the
# programs can be efficient, they often break one of the critical tenants of python: keep it simple, stupid. However,
# classes are an invaluable aspect of OOP that leads to enhanced functionality while retaining readability. According to
# PEP8, the class name should be in camel case and does not require parentheses if no arguments are provided.
# Additionally, a class requires an action to be created, so the `pass` command is often used to initially create the
# framework of the class before the underlying functions are created.


class DoesNothing:
    """
    The `pass` command does nothing, but an action is required to create a class. The `pass` command acts as the
    required action.
    """
    pass


# Prints the type of the class
print(type(DoesNothing))
# Prints the type of the function of the class. Since no functions are declared, only `__main__` is provided.
print(type(DoesNothing()))

# Classes are an effective way to structure data that can be easily retrieved using custom methods. This is similar to
# the data structure of a tuple or a dictionary, but with enhanced functionality.

# Tuple
tuple_example = ("Adam West", "Burt Ward")
# Dictionary
dictionary_example = {"batman": "Adam West", "robin": "Burt Ward"}


class CantGetRidOfABomb:
    def __init__(self, role, actor):
        """
        The class begins with the `.__init__()` method to initialize the variables.
        :param role: Name of the role played by the actor.
        :param actor: Name of the actor associated with the role.
        """
        self.role = role
        self.actor = actor


man_of_bats = CantGetRidOfABomb("batman", "Adam West")
boy_wonder = CantGetRidOfABomb("robin", "Burt Ward")
p_n_guin = CantGetRidOfABomb(role="penguin", actor="Danny DeVito")

# Tuples do not have any named positions, so the data must be contained in the same location every time.
print(tuple_example[0])
print(tuple_example[1])

# Dictionaries have named positions, but are immutable and cannot have new entries appended.
print(dictionary_example["batman"])
print(dictionary_example["robin"])

# Classes can pull the information based on custom functions. This has enhanced readability and functionality.
print("{} plays {}".format(man_of_bats.actor, man_of_bats.role))
print("{} plays {}".format(boy_wonder.actor, boy_wonder.role))

# Tuples cannot have additional items appended to the existing list.
tuple_example.append("Burgess Meredith")

# Dictionaries can add additional key/value pairs or update existing easily through calling the key.
dictionary_example["penguin"] = "Danny DeVito"
print(dictionary_example["penguin"])
dictionary_example["penguin"] = "Burgess Meredith"
print(dictionary_example["penguin"])

# Classes can also update existing entries easily.
p_n_guin = CantGetRidOfABomb(role="penguin", actor="Burgess Meredith")
print("{} plays {}".format(p_n_guin.actor, p_n_guin.role))

# Classes also have the ability to be added to a list to record the names of the class objects, which also allows for
# the .append() method to be used.
class_list = [man_of_bats, boy_wonder, p_n_guin]
print("{} plays {}".format(class_list[0].actor, class_list[0].role))
class_list.append(CantGetRidOfABomb(actor="Cesar Romero", role="joker"))
print("{} plays {}".format(class_list[-1].actor, class_list[-1].role))

# Unlike dictionaries and lists, classes can contain additional functions that are applied to the inputs. Without
# classes, the level of complexity required to achieve high level functionality would render the application improbable
# to develop.


class Doggo:

    def __init__(self, name):
        """
        Initializes the objects of the class.
        :param name: Name of the doggo is the only required input.
        """
        self.name = name
        self.tricks = []  # creates a new empty list for each dog

    def add_trick(self, trick):
        """
        Appends the trick to the list associated with the specific dog.
        :param trick: Trick that the dog knows
        :return: Appends the supplied trick to the tricks list for the dog by name.
        """
        self.tricks.append(trick)


boykin = Doggo('Captain Jack Barkness')
boykin.add_trick('stand')
boykin.add_trick('high five')
boykin.add_trick('shake')
boykin.add_trick('be super hyper')

og_boykin = Doggo('Savien')
og_boykin.add_trick('roll over')
og_boykin.add_trick('sit')
og_boykin.add_trick('shake')
og_boykin.add_trick('be the best of boys')

print("{} knows the tricks: {}".format(boykin.name, boykin.tricks))
print("{} knows the tricks: {}".format(og_boykin.name, og_boykin.tricks))

#OOP primarily revolves around Classes, Function, and Decorators

#a decroator is a function that leverages another functon without changing it 


def bar():
    print("This is the bar()")


def foo(f):
    print("This is the foo()")
    f()
    print("This is the function name: {}".format(f.__name__))


foo(bar)

#The "pie" syntax (@) is an easier method of using decorators. 
#The "pie" syntax can be used to declare the function being called as the declarator, followed by the function used as an input to the declarator
#The declarator functions need to be executed before the "pie" syntax command


def foo(f):
    print("This is the foo()")
    f()
    print("This is the function name: {}".format(f.__name__))


@foo
def bar():
    print("This is the bar()")

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
        Internal function toi call the decoration function and calculate program time.
        :param args: Can accept positional arguments to call the decoration function.
        :param kwargs: Can accept keyword arguments to call the decoration function.
        :return: Prints the time taken with embedded wait from the decoration function.
        """
        t = time.time()
        f(*args, **kwargs)
        print("{} () took {} to complete.".format(f.__name__, time.time() - t))
    return calc_time


# Decorator declration
f = program_time(waiting)

f() #Calls the function with the default value as the waiting argument
f(1) #Calls the function with the waiting argument set as 1 second
f(t=5) #Calls the function with the waiting argument set as 5 seconds 
print("Output of calling __name__ on decorator `f`: {}. This differs from the __name__ of the function when it is "
      "called in the calc_time() function.".format(f.__name__))


#A class requires an action to be created, so the pass command is often used to initially create the framework
class DoesNothing:
    """
    The pass command does nothing, but an action is required
    """
    pass


#Prints the type of the class
print(type(DoesNothing))
#Prints the type of the function of the class. Since no functions are declared, only main is provided
print(type(DoesNothing()))

#Classes are an effective way to structure data that can be easily retrieved using custom methods. 
# This is similar to the data structure of a tuple or a dictionary, but with enhanced functionality.

#tuple
tuple_example = ("Adam West", "Burt Ward", "Burgess Meredith")
#dictionary 
dictionary_example = {"batman": "Adam West", "robin": "Burt Ward", "penguin": "Burgess Meredith"}


class CantGetRidOfABomb:
    def __init__(self, role, actor):
        """
        The class begins with the __init__ method to initialize the variables. 
        :param role: Name of the role played by the actor.
        :param actor: Name of the actor associated with the role. 
        """
        self.role = role
        self.actor = actor


man_of_bats = CantGetRidOfABomb("batman", "Adam West")
boy_wonder = CantGetRidOfABomb("robin", "Burt Ward")

#tuples do not have any named positions, so the data must be contained in the same location everytime 
print(tuple_example[0])
print(tuple_example[1])

#dictionaries have named positions, but are immutable and cannot have new entries appended
print(dictionary_example["batman"])
print(dictionary_example["robin"])

#classes can pull the information based on custom functions. This has enhanced readability and functionality
print("{} plays {}".format(man_of_bats.actor, man_of_bats.role))
print("{} plays {}".format(boy_wonder.actor, boy_wonder.role))

#tuples cannot have additional items appended to the existing list
# tuple_example.append("Burgess Meredith")

#dictionaries can add additional key/value pairs or update existing easily through calling the key
dictionary_example["penguin"] = "Danny DeVito"
print(dictionary_example["penguin"])
dictionary_example["penguin"] = "Burgess Meredith"
print(dictionary_example["penguin"])

#classes can also update existing entries easily
p_n_guin = CantGetRidOfABomb(role="penguin", actor="Burgess Meredith")
print("{} plays {}".format(p_n_guin.actor, p_n_guin.role))

#Classes also have the ability to be added to a list to record the names of the class objects, which also allows for the .append() method to be used.

class_list = [man_of_bats, boy_wonder, p_n_guin]
print("{} plays {}".format(class_list[0].actor, class_list[0].role))
class_list.append(CantGetRidOfABomb(actor="Cesar Romero", role="joker"))
print("{} plays {}".format(class_list[-1].actor, class_list[-1].role))

#Unlike dictionaries and lists, classes can contain additional functions that are applied to the inputs
class Doggo:

    def __init__(self, name):
        """
        Initialized the ojects of the class
        :param name: Name of the doggo is the only required input
        """
        self.name = name
        self.tricks = [] #creates a new empty list for each dog

    def add_trick(self, trick):
        """
        Appends the trick to the list associated with the specific dog
        :param trick: trick that the dog knows
        :return: Appends the supplied trick to the tricks list for the dog by name
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
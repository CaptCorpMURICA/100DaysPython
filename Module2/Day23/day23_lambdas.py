#Lambda expressions are used to create a condensed function within a python expression
from typing import List 


def odds(x:int) -> List:
    """
    Use a lambda function to provide a list of odd values between 0 and a maximum received from the user
    :param x: Integer
    :return: List of odd integers from zero to the provided maximum. 
    """
    return list(filter(lambda x: x % 2, range(x)))


#an example of the task using a loop
odd = []
n = int(input("Please provide a positive number greater than zero: "))
for i in range(n):
    if i % 2 != 0:
        odd.append(i)
print("For Loop: {}".format(odd))
print("Lambda Function: {}".format(odds(n)))
print("Lambda Expression: {}".format(list(filter(lambda n: n % 2, range(n)))))

#Lambda expressions take the form of lambda [parameter_list]: expression. 
#This is equivalent to function declarations with the form of def function_name([parameter_list]): return expression. 
#The adder and casing examples display the same functionality between the two methods. 
#addition example of function vs lambda


def adder(x: int, y: int) -> int:
    """
    Adds two integers together
    :param x: integer
    :param y: integer
    :return: The sum of the two integer inputs.
    """
    return x + y


x = 1100
y = 17
add = lambda x, y: x + y

print("Function: {}\nLambda: {}".format(adder(x, y), add(x, y)))

print("=" * 100)

# Casing example of function vs lambda


def prop_case(s: str) -> str:
    """
    Take a string input and convert it to the proper casing structure using the `.capitalize()` method.
    :param s: String in the received casing structure
    :return: The string converted into the proper casing structure
    """
    return s.capitalize()


s = str(input("Provide a string to convert to the proper casing structure."))
pcase = lambda s: s.capitalize()
print("Function: {}\nLambda: {}".format(prop_case(s), pcase(s)))
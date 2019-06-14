# Day 23: Lambdas 
**Instructions:** 
1. Open a new python file.
2. Lambda functions are a way to condense multiple lines of python code into a single line; they can be used wherever normal function objects are required. While this usually reduces overall readability, it is a common challenge for python developers to try and write programs in the fewest lines possible. This type of exercise greatly improves the skill level of the developer because they can often conceptualize how to approach a solution in more unique ways. This often leads to more creative and efficient python programs. Additionally, an equally beneficial challenge is to take an existing program that uses lambdas and refactor it to remove all lambda expressions (Fredrik Lundh provides a refactoring recipe in the [Functional Programming How To](http://docs.python.org/3/howto/functional.html) guide). This refactoring method will instill a stronger understanding of when lambda expressions are appropriate and why they should be used.
3. Lambda expressions are used to create a condensed function within a python expression. A loop that calculates and displays the odd numbers. While this can be done easily in a loop, it takes five lines to complete the task. If using a lambda statement in a function, it only takes three lines to accomplish the same task. While this is a more condensed command, the process is more difficult to understand. The `for` loop clearly indicates that if the remainder of `i` by 2 is not equal to zero, it indicates that `i` is an odd number. This number is then added to a list and the loop continues. The function uses the `filter()` function to ignore `x` where the remainder of `x` by 2 within the range of `x`. These numbers are then turned into a list and returned. Both methods solve the same problem, but one is substantially more difficult to understand.  Additionally, the lambda expression can be used on its own. This final print statement shows that the entire process can be reduced to a single line of code.
    ```
    from typing import List


    def odds(x: int) -> List:
        """
        Use a lambda function to provide a list of odd values between 0 and a maximum received from the user.
        :param x: Integer
        :return: List of odd integers from zero to the provided maximum.
        """
        return list(filter(lambda x: x % 2, range(x)))


    # An example of the task using a loop
    odd = []
    n = int(input("Provide a positive number greater than zero: "))
    for i in range(n):
        if i % 2 != 0:
            odd.append(i)
    print("For Loop: {}".format(odd))
    print("Lambda Function: {}".format(odds(n)))
    print("Lambda Expression: {}".format(list(filter(lambda n: n % 2, range(n)))))
    ```
4. Lambda expressions take the form of `lambda [parameter_list]: expression`. This is equivalent to function declarations with the form of `def function_name([parameter_list]): return expression`. The adder and casing examples display the same functionality between the two methods. The lambda expression is used to turn `add` into a function which can be called to provide the requested value. However, while the functionality is the same, defining explicit functions has the added benefit of docstrings. This is not a functionality available for lambda expressions.
    ```
    # Addition example of function vs lambda


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
    ```
5. Update the [log file](../../log.md) with what you have learned today.

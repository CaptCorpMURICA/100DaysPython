# Day 20: Functions 
**Instructions:** 
1. Open a new python file.
2. Custom functions are critical for creating complex programs. First, the function needs to be defined and provided a name. The `return` command exports the output from the function to the rest of the python script. According to PEP8, There should be two blank lines before and after the declaration of each function. No actions are taken from the function declaration until it is called. Custom functions need to be declared before the first time they are used. Both the inputs and the outputs of a function are optional. If no output is provided, the function will automatically return `None`. Functions are best utilized for reducing code duplication, improving readability, and reduce the complexity of a program into more manageable chunks.
3. While the "Hello World!" exercise could be completed with only a simple `print()` function, this is an example of the most basic of custom functions. The name of the function is defined with the `def` statement and no inputs are given. The function simply returns a single line of text, so when the function is called in a print statement, the output, "Hello World!", is generated.
    ```
    def hello():
        return "Hello World!"
    
    print(hello())
    ````
4. Functions are used to reduce code duplication. If a block of code is used more than twice, it's best to turn it into a function. This will also eliminate additional risk of failure when modification to the code need to be made. Instead of needing to write the calculation multiple times, the calculations can be completed by making a function call. This reduces the overall error risk by eliminating redundancies. Functions also provide improved readability by containing the transformation logic into a single location.
    ```
    def even(a):
        while a % 2 != 0:
            a *= 2
        return a

    for x in [3, 35, 2, 107, 254]:
        if x == even(x):
            print(f"{x} is an even number.")
        else:
            print(f"{x} first becomes an even number when it's multiplied by 2 to become {even(x)}.")

    # Creating the same output without using a function. While this is still readable and easy to understand for the simple
    # case, more complex problems quickly become confusing.
    for x in [3, 35, 2, 107, 254]:
        if x % 2 == 0:
            print(f"{x} is an even number.")
        else:
            y = x * 2
            print(f"{x} first becomes an even number when it's multiplied by 2 to become {y}.")
    ```
5. Custom functions can also call other functions. It is important to ensure any dependent functions are declared before the initial execution. Similar to `import` statements, it is best to declare all functions at the beginning of the script.
    ```
    def pythag(a):
        c = (a ** 2 + even(a) ** 2) ** .5
        return c

    x = int(input("Please provide an integer."))
    print(f"Function output: {pythag(x)}.")

    if x % 2 == 0:
        man_a = x
        man_b = x
    else:
        man_a = x
        man_b = x * 2
    print(f"Manual Calculation: a = {man_a}, b = {man_b}, c = {(man_a ** 2 + man_b ** 2) ** .5}")
    ```
6. Complex functions can be created to completed tasks like matrix addition. This example raises exceptions if improper matrices are provided and uses nested `for` loops to complete the calculation. By turning this complex calculation into a function, it is contained into a single location, is easy to read, and is formatted for quick debugging with seamless integration.
    ```
    def matrix_add(m1, m2):
        if len(m1) != len(m2):
            raise ValueError("Given matrices are not the same size.")
        for i in range(0, len(m1)):
            if len(m1[i]) != len(m2[i]):
                raise ValueError("Given matrices are not the same size.")
            for j in range(0, len(m1[0])):
                m1[i][j] = (m1[i][j] + m2[i][j])
        return m1

    matrix1 = [[1, -2], [-3, 4]]
    matrix2 = [[2, -1], [0, -1]]
    print(matrix_add(matrix1, matrix2))
    ```
7. It is critical that custom functions include [docstrings](https://www.python.org/dev/peps/pep-0257/). This adds built-in documentation for the function which assists the user in correct implementation and improves understanding of functionality.
    ```
    def matrix_mult(m1, m2):
        """
        This function accepts two matrices of any, but equal size and multiplies the values at each identical index.

        e.g.
        matrix1 = [[1, -2], [-3, 4]]
        matrix2 = [[2, -1], [0, -1]]
        returns: [[2, 2], [0, -4]]

        :param m1: A list of lists (i.e. a matrix). Can only contain numeric values.
        :param m2: A list of lists (i.e. a matrix) of the same size as m1. Can only contain numeric values.
        :return: matrix1 * matrix2
        """
        if len(m1) != len(m2):
            raise ValueError("Given matrices are not the same size.")
        for i in range(0, len(m1)):
            if len(m1[i]) != len(m2[i]):
                raise ValueError("Given matrices are not the same size.")
            for j in range(0, len(m1[0])):
                m1[i][j] = (m1[i][j] * m2[i][j])
        return m1
    ```
8. By using the `.__doc__` object, the docstring can be printed for any function. Additionally, the `help()` function returns the docstring. The `help()` function is the primary method of obtaining the docstring on classes and their underlying methods or functions.
    ```
    print(matrix_mult.__doc__)
    print(help(matrix_mult))
    ```
9. Type hints do not change the fact that variables in python are mutable, but instead provide guidance on the expected variable types for the inputs and outputs of a function. This information also becomes available within the built-in documentation and autocomplete hints. Additional types can be used for type hints through importing the `typing` module by executing `from typing import X` where _X_ is replaced with the desired type (e.g. Tuple, List, etc.).
    ```
    def multi_out(a: int) -> [int, float]:
        """
        Takes an integer, adds two, and then calculates the hypotenuse based on the two previous values.
        :param a: int
        :return: b: int (a + 2)
                 c: float (hypotenuse of a and b)
        """
        b = a + 2
        c = (a ** 2 + b ** 2) ** .5
        return b, c

    a = 5
    b, c = multi_out(a)
    print(f"Two more than {a} is {b} and the hypotenuse of those two is {c:.2f}.")
    ```
10. Update the [log file](../../log.md) with what you have learned today.

#custom functions are critical for creating complex programs
#the function needs to be defined and provided a name
#the return command exports the output to the rest of the python script
#there should always be two blank lines before and after the declaration of each function
#no actions are taken from the function declaration until it is called 
#functions are best for creating more manageable chunks of code in a script

#the name of the function is defined with the def statement, here no inputs are given

def hello():
    return "Hello World!"

print(hello())

#functions reduces the overall error risk by eliminating redundancies

def even(a):
    while a % 2 != 0:
        a *= 2 
    return a

for x in [3, 35, 2, 107, 254]:
    if x == even(x):
        print(f"{x} is an even number.")
    else: 
        print(f"{x} first becomes an even number when it's multiplied by 2 to become {even(x)}.")

#creating the same output without using a function
for x in [3, 35, 2, 107, 254]:
    if x % 2 ==0:
        print(f"{x} is an even number.")
    else:
        y = x * 2
        print(f"{x} first becomes an even number when it's multiplied by 2 to become {y}.")

#custom functions can also call other functions, it is best to declare all functions at the beginning of the script

def pythang(a):
    c = (a ** 2 + even(a) ** 2) ** .5
    return c

x = int(input("Please provide any integer."))
print(f"Function output: {pythang(x)}.")

if x % 2 == 0:
    man_a = x
    man_b = x
else: 
    man_a = x
    man_b = x * 2
print(f"Manual Calculation: a = {man_a}, b = {man_b}, c = {(man_a ** 2 + man_b ** 2) ** .5}")

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

print(matrix_mult.__doc__)
print(help(matrix_mult))

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
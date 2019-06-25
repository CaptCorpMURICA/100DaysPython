def factorial(n: int) -> int:
    """
    Calculate the factorial of an integer greater than zero.
    :param n: Must be an integer greater than zero.
    :return: The integer value of N!
    """

    if n < 0:
        print("n must be a positive number. {} is an invalid response.".format(n))
        exit(code=1)
    if n in (0, 1):
        return 1
    return factorial(n -1) * n


n = int(input("Provide an integer for factorial calculation: "))

soln = 1 
for i in range(0, n +1):
    if n < 0:
        print("n must be a positive number. {} is an invalid response.".format(n))
        break
    if i in (0, 1):
        soln = 1
        continue
    soln *= i

print("""{}!
Recursion Results: {}
Loop Results: {}""".format(n, factorial(n), soln))

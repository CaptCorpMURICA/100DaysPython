"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module2_day21_pytest.py
    Creation Date:  6/11/2019, 8:20 PM
    Description:    Contains the function to be tested by PyTest.
"""


class BasicCalc:
    """
    A program to complete basic addition, subtraction, multiplication, and division of two numbers.
    """

    def add(self, a: float, b: float) -> float:
        if type(a) != float and type(a) != int and type(b) != float and type(b) != int:
            raise TypeError("The value provided is not a number.")
        return a + b

    def subtract(self, a: float, b: float) -> float:
        if type(a) != float and type(a) != int and type(b) != float and type(b) != int:
            raise TypeError("The value provided is not a number.")
        return a - b

    def multiply(self, a: float, b: float) -> float:
        if type(a) != float and type(a) != int and type(b) != float and type(b) != int:
            raise TypeError("The value provided is not a number.")
        return a * b

    def divide(self, a: float, b: float) -> float:
        if type(a) != float and type(a) != int and type(b) != float and type(b) != int:
            raise TypeError("The value provided is not a number.")
        try:
            return a / b
        except ZeroDivisionError:
            return ZeroDivisionError.__name__

    def quit(self, a: int, b: int):
        print("Thank you for using the Python Calculator 9000\nGood bye.")
        quit(0)


if __name__ == "__main__":
    print("Python Calculator 9000")
    calculator = BasicCalc()
    operation = {"1": calculator.add,
                 "2": calculator.subtract,
                 "3": calculator.multiply,
                 "4": calculator.divide,
                 "5": calculator.quit
                 }
    while True:
        for choice, operator in sorted(operation.items()):
            print("{}: {}".format(choice, operator.__name__))
        selection = input("What type of operation do you want to do?")
        if selection not in operation:
            print("That is not a valid option. Please try again.")
            continue

        if selection == "5":
            a = 0
            b = 0
        else:
            a = float(input("What is your first number?"))
            b = float(input("What is your second number?"))

        if a == '' or b == '':
            print("Both values need to be provided. Please try again.")
            continue

        print("{}: {}, {} equals {}".format(selection, a, b, operation[selection](a, b)))

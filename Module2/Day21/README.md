# Day 21: Pytest
**Instructions:** 
1. Open a new python file.
2. With each program created, it is critical that robust testing is performed. The time for testing code is not when it is in production and the best method is to automate the checks. The python standard library contains the [unittest](https://docs.python.org/3/library/unittest.html) package. While this has the advantage of being packaged with python, it is not the best framework available. One of the most widely used testing frameworks in [pytest](https://docs.pytest.org/en/latest/). Since this is not included in the standard library, it will first need to be installed. This is a brief introduction into creating tests for your application; for more information, research Brian Okken through his [website](http://pythontesting.net/) or [podcast](https://testandcode.com/).
3. Pytest primarily uses `assert` statements to test functions in the module. This allows the developer to determine different cases in which the program should succeed or fail. If you are creating a program that changes functionality based on the time of day or year, pytest can be used to simulate those conditions instead of needing to wait in real time. The testing code is separated from the rest of the program in a separate file. This testing file should start with `test_` or end with `_test.py`.
4. First import the pytest package and then import the function to be tested from the other file.
    ```
    import pytest
    from module2_day21_pytest import BasicCalc
    ```
5. Each test is declared as a separate function. The purpose of each function is to push specific parameters to the program to identify if the desired results were received. These tests should encompass scenarios that will lead to a success as well as a failure. Making sure the program doesn't work when it's not supposed to work is just as important.
    ```
    def test_add():
        calculator = BasicCalc()
        result = calculator.add(2, 2)
        assert result == 4

    def test_subtract():
        calculator = BasicCalc()
        result = calculator.subtract(2, 2)
        assert result == 0

    def test_multiply():
        calculator = BasicCalc()
        result = calculator.multiply(2, 2)
        assert result == 4

    def test_divide():
        calculator = BasicCalc()
        result = calculator.divide(2, 2)
        assert result == 1

    def test_zero_div():
        calculator = BasicCalc()
        result = calculator.divide(5, 0)
        assert result == "ZeroDivisionError"
    
    def test_will_fail():
        calculator = BasicCalc()
        result = calculator.add(2, 2)
        assert result == 5
    ```
6. Tests can be explicitly failed by using the `.fail()` function. This is useful when building the framework of tests, but the specifics aren't yet developed (or the functionality to be tested isn't yet built).
   ```
   def test_man_fail():
       calculator = BasicCalc()
       with pytest.fail("I made this one fail."):
           calculator.add(2, 2)
   ```
7. Pytest can look for errors by using the `.raises()` function. This is extremely useful when validating the program functions as designed if inputs are received that break the program.
   ```
   def test_str():
       calculator = BasicCalc()
       with pytest.raises(TypeError):
           calculator.divide("four", 2)
   ```
8. Update the [log file](../../log.md) with what you have learned today.

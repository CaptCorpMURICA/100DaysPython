"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module2_day21_pytest_test.py
    Creation Date:  6/11/2019, 8:13 PM
    Description:    Learn the basics of pytest. This will conduct tests on the module2_day21_pytest.py file.
"""

import pytest
from module2_day21_pytest import BasicCalc


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


def test_man_fail():
    calculator = BasicCalc()
    with pytest.fail("I made this one fail."):
        calculator.add(2, 2)


def test_str():
    calculator = BasicCalc()
    with pytest.raises(TypeError):
        calculator.divide("four", 2)

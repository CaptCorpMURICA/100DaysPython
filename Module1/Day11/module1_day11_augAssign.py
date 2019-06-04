
"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module1_day11_augAssign.py
    Creation Date:  6/2/2019, 8:55 AM
    Description:    Learn about augmented assignments in python.
                    +=  : Addition
                    -=  : Subtraction
                    *=  : Multiplication
                    /=  : Division
                    //= : Floor Division
                    %=  : Remainder/Modulus
                    **= : Exponent
                    <<= : Left Shift
                    >>= : Right Shift
                    &=  : And
                    ^=  : Exclusive Or (XOR)
                    |=  : Inclusive Or (OR)
"""
# The addition operator is used to replace a variable with the value plus the supplied amount.
x = 42
x += 3
print(x)

# The subtraction operator is used to replace a variable with the value minus the supplied amount.
x = 42
x -= 3
print(x)

# The multiplication operator is used to replace a variable with the value times the supplied amount.
x = 42
x *= 3
print(x)

# The division operator is used to replace a variable with the value divided by the supplied amount.
x = 42
x /= 3
print(x)

# The floor division operator is used to replace a variable with the floor integer of the value divided by the supplied
# amount.
x = 42
x //= 3
print(x)

# The modulus operator is used to replace a variable with the remainder of the value divided by the supplied amount.
x = 42
x %= 3
print(x)

# The exponent operator is used to replace a variable with the value to the power of the supplied amount.
x = 42
x **= 3
print(x)

# The left shift operator is a bitwise operator that replaces the value of the variable with the value of the bitwise
# left shift equal to the number of the supplied amount. This is not an operation that will be used throughout the rest
# of this course, but I recommend researching bitwise operations to understand a potential use case.
x = 1
x <<= 2
print(x)

# The right shift operator is a bitwise operator that replaces the value of the variable with the value of the bitwise
# right shift equal to the number of the supplied amount. This is not an operation that will be used throughout the rest
# of this course, but I recommend researching bitwise operations to understand a potential use case.
x = 4
x >>= 1
print(x)

# The AND bitwise operator assigns the result of the AND operation to the left operand.
x = True
y = False
x &= y
print(x)

# The exclusive OR bitwise operator assigns the result of the XOR operation to the left operand.
x = True
y = False
x ^= y
print(x)

# The inclusive OR bitwise operator assigns the result of the OR operation to the left operand.
x = True
y = False
x |= y
print(x)

# The addition and multiplication augmented assignments can also be used on strings for addition and multiplication
# concatenation operations.
x = "Ten Million "
y = "Dollars"
x *= 3
x += y
print(x)

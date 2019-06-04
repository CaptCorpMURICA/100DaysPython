# Day 11: Augmented Assignments
**Instructions:** 
1. Open a new python file.
2. An augmented assignment improves efficiency because python can iterate a single variable instead of using a temporary one.
3. There are several types of augmented assignment operators:  
   \+=  : Addition  
   \-=  : Subtraction  
   \*=  : Multiplication  
   \/=  : Division  
   \//= : Floor Division  
   \%=  : Remainder/Modulus  
   \**= : Exponent  
   \<<= : Left Shift  
   \>>= : Right Shift  
   \&=  : And  
   \^=  : Exclusive Or (XOR)  
   \|=  : Inclusive Or (OR)
4. The **addition** operator is used to replace a variable with the value plus the supplied amount. _Type and execute:_  
   `x = 42`  
   `x += 3`  
   `print(x)`
5. The **subtraction** operator is used to replace a variable with the value minus the supplied amount. _Type and execute:_  
   `x = 42`  
   `x -= 3`  
   `print(x)`
6. The **multiplication** operator is used to replace a variable with the value times the supplied amount. _Type and execute:_  
   `x = 42`  
   `x *= 3`  
   `print(x)`
7. The **division** operator is used to replace a variable with the value divided by the supplied amount. _Type and execute:_  
   `x = 42`  
   `x /= 3`  
   `print(x)`
10. The **floor division** operator is used to replace a variable with the floor integer of the value divided by the supplied amount. _Type and execute:_  
   `x = 42`  
   `x //= 3`  
   `print(x)`
9. The **modulus** operator is used to replace a variable with the remainder of the value divided by the supplied amount. _Type and execute:_  
   `x = 42`  
   `x %= 3`  
   `print(x)`
10. The **exponent** operator is used to replace a variable with the value to the power of the supplied amount. _Type and execute:_  
   `x = 42`  
   `x **= 3`  
   `print(x)`
11. The **left shift** operator is a bitwise operator that replaces the value of the variable with the value of the bitwise left shift equal to the number of the supplied amount. This is not an operation that will be used throughout the rest of this course, but I recommend researching [bitwise operations](https://en.wikipedia.org/wiki/Bitwise_operation) to understand a potential use case. _Type and execute:_  
   `x = 1`  
   `x <<= 2`  
   `print(x)`
12. The **right shift** operator is a bitwise operator that replaces the value of the variable with the value of the bitwise right shift equal to the number of the supplied amount. This is not an operation that will be used throughout the rest of this course, but I recommend researching [bitwise operations](https://en.wikipedia.org/wiki/Bitwise_operation) to understand a potential use case. _Type and execute:_  
   `x = 4`  
   `x >>= 1`  
   `print(x)`
13. The **AND** bitwise operator assigns the result of the AND operation to the left operand. _Type and execute:_  
   `x = True`  
   `y = False`  
   `x &= y`  
   `print(x)`
14. The **exclusive OR** bitwise operator assigns the result of the XOR operation to the left operand. _Type and execute:_  
   `x = True`  
   `y = False`  
   `x ^= y`  
   `print(x)`
15. The **inclusive OR** bitwise operator assigns the result of the OR operation to the left operand. _Type and execute:_  
   `x = True`  
   `y = False`  
   `x |= y`  
   `print(x)`
16. The addition and multiplication augmented assignments can also be used on strings for addition and multiplication concatenation operations. _Type and execute:_  
   `x = "Ten Million "`  
   `y = "Dollars"`  
   `x *= 3`  
   `x += y`  
   `print(x)`
17. Update the [log file](../../log.md) with what you have learned today.

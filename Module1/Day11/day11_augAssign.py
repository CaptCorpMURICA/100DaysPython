#An augmented assignment improves efficiency because python can iterate a single variable instead of using a temporary one.
#There are several types of augmented assignment operators:
# += : Addition
# -= : Subtraction
# *= : Multiplication
# /= : Division
# //= : Floor Division
# %= : Remainder/Modulus
# **= : Exponent
# <<= : Left Shift
# >>= : Right Shift
# &= : And
# ^= : Exclusive Or (XOR)
# |= : Inclusive Or (OR)

x = 42 
x += 3
print(x)

x = 42
x -= 3
print(x)

x = 42
x *= 3
print(x)

x = 42
x /= 3
print(x)


x = 42 
x //= 3
print(x)

x = 42 
x %= 3
print(x)

x = 42
x **= 3
print(x)

x = 1
x <<= 2
print(x)

x = 4
x >>= 1
print(x)

x = True 
y = False
x &= y
print(x)

x = True 
y = False
x ^= y
print(x)

x = True 
y = False
x |= y
print(x)

x = "Ten Million"
y = "Dollars"
x *= 3
x += y
print(x)
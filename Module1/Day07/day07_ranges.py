#the endpoint of a range is not inclusive
print(range(10))
print(list(range(10)))
print(range(0, 9, 2) == range(0, 10, 2))

#range declaration has the format range(start, stop, step)
even = range(0, 10, 2)
odd = range(1, 10, 2)

print(f"The even range is {even} and the values are {list(even)}")
print(f"The even range is {odd} and the values are {list(odd)}")

#if the step is negative, then the range values are produced in reverse, the higher number msut be in the start position
even = range(10, 0, -2)
odd = range(9, 0, -2)

print(f"The even range is {even} and the values are {list(even)}")
print(f"The even range is {odd} and the values are {list(odd)}")

#a range can be used to identify a collection of numbers divisible by a specific value
val = int(input("Please provide a whole number for the divisibility check: "))
request = int(input("Please provide a whole number, less than 1 million, that is to be tested for divisbility: "))
in_range = range(val, 1000000, val)

if request > 1000000:
    print("Please select a number less than 1 million and try again. Thank you")
elif request in in_range:
    print(f"{request} is divisible by {val}.")
else:
    print(f"{request} is not divisible by {val}.")

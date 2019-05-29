# Day 7: Ranges
**Instructions:** 
1. Open a new python file.
2. A range starts with an index of 0 and ends with the declared value. The endpoint of a range in not inclusive. Therefore, the range will contain indices from 0 to 41, but it will not use 42. _Type and execute:_  
   `print(range(10))`  
   `print(list(range(10)))`  
   `print(range(0, 9, 2) == range(0, 10, 2))`
3. The range declaration has the format `range(start, stop, step)`. _Type and execute:_  
   `even = range(0,10,2)`  
   `odd = range(1,10,2)`  
   `print("The even range is {} and the values are {}".format(even, list(even)))`  
   `print("The odd range is {} and the values are {}".format(odd, list(odd)))`
4. If the step is negative, then the range values are produced in reverse. The higher number must be in the start position if producing results in reverse. _Type and execute:_  
   `even = range(10,0,-2)`  
   `odd = range(9,0,-2)`  
   `print("The even range is {} and the values are {}".format(even, list(even)))`  
   `print("The odd range is {} and the values are {}".format(odd, list(odd)))`
5. By using a specific step value, a range can be used to identify a collection of numbers divisible by a specific value. This example uses the `input()` function to prompt the user for input. It also used `if/elif/else` statements, which will be covered on [Day 10](../Module1/Day10). _Type and execute:_  
   `val = int(input("Please provide a whole number for the divisibility check: "))`  
   `request = int(input("Please provide a whole number, less than 1 million, that is to be tested for divisibility: "))`  
   `in_range = range(val, 1000000, val)`
   `if request > 1000000:`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("Please select a number less than 1 million and try again. Thank you")`  
   `elif request in in_range:`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("{} is divisible by {}.".format(request, val))`  
   `else:`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("{} is not divisible by {}.".format(request, val))`
6. Update the [log file](../../log.md) with what you have learned today.

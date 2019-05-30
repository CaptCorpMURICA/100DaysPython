# Day 9: Index and Slicing
**Instructions:** 
1. Open a new python file.
2. Specific items can be retrieved from a list by using its indices. _Type and execute:_  
   `quotes = ["Pitter patter, let's get at 'er", "Hard no!", "H'are ya now?", "Good-n-you?", "Not so bad.", "Is that what you  appreciates about me?"]`    
   `quotes[0]`  
   `print(f"{quotes[2]}\n\t{quotes[3]}\n{quotes[4]}")`
3. Slicing uses the format `[start:stop:step]`. Start is _inclusive_, but stop is _exclusive_. Unlike using just the index, slicing allows the user to return a sequence rather than a single item. Slicing can be conducted on mutable and immutable objects. _Type and execute:_  
   `quotes[2:5]` 
4. The step can be used to identify how many items to skip between returned values. _Type and execute:_  
   `quotes[::2]`
5. The step can also be used to reverse the order of the returned items. _Type and execute:_  
   `quotes[::-1]`
6. Slicing can be combined with indices to return a sequence from a specific item. _Type and execute:_  
   `quotes[0][::2]`  
   `quotes[0][::-1]`
7. _Type and execute:_  
   `wayne = "Toughest Guy in Letterkenny"`  
   `wayne[::-1]`
8. Retrieval by index and slicing can also be applied directly to a string. _Type and execute:_  
   `"That's a Texas sized 10-4."[0:9:2]`
9. 
10. 
11. 
12. 
13. 
14. 
15. Update the [log file](../../log.md) with what you have learned today.

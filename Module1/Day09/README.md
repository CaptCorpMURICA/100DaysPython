# Day 9: Index and Slicing
**Instructions:** 
1. Open a new python file.
2. Specific items can be retrieved from a list by using its indices.
    ```
    quotes = ["Pitter patter, let's get at 'er", "Hard no!", "H'are ya now?", "Good-n-you?", "Not so bad.", "Is that what you appreciates about me?"]
    quotes[0]
    print(f"{quotes[2]}\n\t{quotes[3]}\n{quotes[4]}")
    ```
3. Slicing uses the format `[start:stop:step]`. Start is _inclusive_, but stop is _exclusive_. Unlike using just the index, slicing allows the user to return a sequence rather than a single item. Slicing can be conducted on mutable and immutable objects.  
    `quotes[2:5]`
4. The step can be used to identify how many items to skip between returned values.  
    `quotes[::2]`
5. The step can also be used to reverse the order of the returned items.  
    `quotes[::-1]`
6. Slicing can be combined with indices to return a sequence from a specific item.
    ```
    quotes[0][::2]
    quotes[0][::-1]
    ```
7. Slicing doesn't only need to be applied to lists. It can also be used on variables.
    ```
    wayne = "Toughest Guy in Letterkenny"
    wayne[::-1]
    ```
8. Retrieval by index and slicing can also be applied directly to a string.  
    `"That's a Texas sized 10-4."[0:9:2]`
9. Neither the start, nor the stop values are required when slicing.
    ```
    quotes[:]
    quotes[3:]
    quotes[:3]
    quotes[::3]
    ```
10. New list can be created based on the slicing output.
    ```
    exchange = quotes[2:5]
    print(exchange)
    ```
11. Update the [log file](../../log.md) with what you have learned today.

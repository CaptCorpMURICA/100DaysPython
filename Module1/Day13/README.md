# Day 13: Continue/Break
**Instructions:** 
1. Open a new python file.
2. Print only consonants from a given text. _Type and execute:_  
   `motivation = "Over? Did you say 'over'? Nothing is over until we decide it is! Was it over when the Germans bombed Pearl Harbor? Hell no! And it ain't over now. 'Cause when the goin' gets tough...the tough get goin'! Who's with me? Let's go!"`  
   `output = ""`  
   `for letter in motivation:`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`if letter.lower() in 'bcdfghjklmnpqrstvwxyz':`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`output += letter`  
   `print(output)`
3. However, this example can also be completed by using a `continue` action. If the condition is met, then the `continue` advances the program to the next stage. _Type and execute:_  
   `motivation = "Over? Did you say 'over'? Nothing is over until we decide it is! Was it over when the Germans bombed Pearl Harbor? Hell no! And it ain't over now. 'Cause when the goin' gets tough...the tough get goin'! Who's with me? Let's go!"`  
   `output = ""`  
   `for letter in motivation:`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`if letter.lower() not in 'bcdfghjklmnpqrstvwxyz':`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`continue`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`else:`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`output += letter`  
   `print(output)`
4. Conversely, the `break` action halts the program when the condition is met. For instance, what if we wanted to display all of the letters until the first instance of a non-letter? A `break` can be used to end the loop once the condition is met. _Type and execute:_  
   `motivation = "Over? Did you say 'over'? Nothing is over until we decide it is! Was it over when the Germans bombed Pearl Harbor? Hell no! And it ain't over now. 'Cause when the goin' gets tough...the tough get goin'! Who's with me? Let's go!"`  
   `output = ""`  
   `for letter in motivation:`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`if letter.lower() not in 'abcdefghijklmnopqrstuvwxyz':`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`output += letter`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`else:`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`break`  
   `print(output)`
5. Update the [log file](../../log.md) with what you have learned today.

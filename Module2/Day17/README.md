# Day 17: User Input
**Instructions:** 
1. Open a new python file.
2. The `input()` function prompts the user for input. The program is paused until the user presses the `Enter` key. _Type and execute:_  
   `print(input())`
3. The text within the `input()` function is the prompt for the user. This can help direct the user to provide a valid input. _Type and execute:_  
   `print(input("How many questions will you get asked?"))`
4. The results from the `input()` function can be stored in a variable for use within the program. _Type and execute:_  
   `name = input("What is your name?")`  
   `print(name)`
5. The `input()` function can be combined with other, previously discussed, functions to create an interactive game. _Type and execute:_  
   `resp = input("Do you approach the bridge keeper? (y/n)")`  
   `if "y" in resp.lower():`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("Those who approach the Bridge of Death must answer me these questions three. There the other side he see.")`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print(input("How do you respond?"))`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`name = input("What is you name?")`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print(name)`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`quest = input("What is you quest?")`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print(quest)`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`answer = input("What is the airspeed velocity of an unladen swallow?")`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`if "african" in answer.lower() or "european" in answer.lower():`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("I...I don't know that!")`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("The bridge keeper is hurtled into the pit and you are free to cross.")`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`elif "i don't know" in answer.lower():`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("{}, you are hurled into the pit and your quest to {} has come to an end.".format(name.capitalize(), quest))`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`elif "wait" in answer.lower():`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("{}, you are hurled into the pit and your quest to {} has come to an end.".format(name.capitalize(), quest))`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`else:`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("'{}' was a good enough answer. You cross the bridge and continue your quest to {}.".format(answer, quest))`  
   `elif "n" in resp.lower():`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("Just like Sir Robin, you soiled your armor you were so scared. You leave the Bridge of Death, defeated by your own cowardice.")`  
   `else:`  
&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("For being unable to provide a Yes or No, you are hurled into the pit and your quest is over.")`
6. Update the [log file](../../log.md) with what you have learned today.

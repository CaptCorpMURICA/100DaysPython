# Day 17: User Input
**Instructions:** 
1. Open a new python file.
2. The `input()` function prompts the user for input. The program is paused until the user presses the `Enter` key.  
   `print(input())`
3. The text within the `input()` function is the prompt for the user. This can help direct the user to provide a valid input.  
   `print(input("How many questions will you get asked?"))`
4. The results from the `input()` function can be stored in a variable for use within the program.
   ```
   name = input("What is your name?")
   print(name)
   ```
5. The `input()` function can be combined with other, previously discussed, functions to create an interactive game.
   ```
   resp = input("Do you approach the bridge keeper? (y/n)")
   if "y" in resp.lower():
      print("Those who approach the Bridge of Death must answer me these questions three. There the other side he see.")
      print(input("How do you respond?"))
      name = input("What is you name?")
      print(name)
      quest = input("What is you quest?")
      print(quest)
      answer = input("What is the airspeed velocity of an unladen swallow?")
      if "african" in answer.lower() or "european" in answer.lower():
         print("I...I don't know that!")
         print("The bridge keeper is hurtled into the pit and you are free to cross.")
      elif "i don't know" in answer.lower():
         print("{}, you are hurled into the pit and your quest to {} has come to an end.".format(name.capitalize(), quest))
      elif "wait" in answer.lower():
         print("{}, you are hurled into the pit and your quest to {} has come to an end.".format(name.capitalize(), quest))
      else:
         print("'{}' was a good enough answer. You cross the bridge and continue your quest to {}.".format(answer, quest))
   elif "n" in resp.lower():
      print("Just like Sir Robin, you soiled your armor you were so scared. You leave the Bridge of Death, defeated by your own cowardice.")
   else:
      print("For being unable to provide a Yes or No, you are hurled into the pit and your quest is over.")
	```
6. Update the [log file](../../log.md) with what you have learned today.

# Day 10: If/Else
**Instructions:** 
1. Open a new python file.
2. Conditional programming is no different than all of the decisions you make in life. _"If I wake up on time, then I'll make breakfast."_ In python, conditional programming takes the form of `if/elif/else`, where the action is indented underneath the condition. The action is completed if the condition is true. The end of the conditional statement requires a colon (`:`) to mark the end of the line. _Type and execute:_  
   `lost = True`  
   `if lost:`  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("We're going to need a montage.")`
3. If the primary condition (`if`) is not met, the action is not completed. An `else` statement can be used to ensure a specific action is taken if the primary condition is not met. _Type and execute:_  
   `lost = False`  
   `if lost:`  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("We're going to need a montage.")`  
    `else:`  
    &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("Celebrate by giving Adrian a kiss.")`
4. Additional conditions can be added by using the `elif` statement. There is no limit to the number of `elif` statements that can be added; however, there can only be a max of one `if` and `else` statement each. Conditions are checked in sequential order and the action is completed at the first `True` condition. _Type and execute (multiple times):_  
   `prompt = input("What do you want to know? Type: "steps" for number of steps at the Art Museum, "bouts" for the major fights he won, or "job" for Rocky's original job.")`  
   `if lower(prompt) == "steps":`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("You need to run up 72 steps to take a picture with Rocky at the Art Museum in Philadelphia.")`  
   `elif lower(prompt) == "bouts":`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("Rocky (1976): Apollo Creed\nRocky II (1979): Apollo Creed\nRocky III (1982): James 'Clubber' Lang\nRocky IV (1985): Ivan Drago\nRocky V (1990): Tommy Gunn\nRocky Balboa (2006): Mason Dixon")`  
   `elif lower(prompt) == "job":`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("Before becoming a professional boxer, Rocky was nothing but a 'bum' that collected payments for a loan shark.")`  
   `else:`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("{} is not an acceptable entry.".format(prompt))`
5. As the number of conditions increases though, the code can begin to become unruly. _Type and execute:_  
   `num = int(input("Select a positive number between 1 and 10: "))`  
   `if num > 10:`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("How can you expect to be the champ if you can't follow directions?")`  
   `elif num < 1:`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("How can you expect to be the champ if you can't follow directions?")`  
   `elif num < 3:`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("Only {} sides of beef? You need to punch more if you plan to be the champ.".format(num))`  
   `elif num < 6:`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("{} sides of beef? That's a good number to punch if you want to be the champ.".format(num))`  
   `elif num < 10:`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("{} sides of beef? Punching that many is a waste. Even if you become the champ, you shouldn't be wasteful.".format(num))`  
   `else:`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("Well, that shouldn't have happened. {} caused an error.".format(num))`
6. In the example above, the message for `3` would make the fourth condition true. Therefore, the program flow would end before reaching subsequent conditions.
7. Nested conditional statements are a way to efficiently segment actions based on a parent condition being met first. _Type and execute:_  
   `awards = input("Which would you like to see, awards won or nominated?")`  
   `if awards.lower() == 'won':`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("Rocky won Oscars for Best Picture, Best Director, and Best Film Editing")`  
   `elif awards.lower() == 'nominated':`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`movie = input("Which movie do you want to hear about, Rocky or Rocky III?)`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`if movie.lower() == 'rocky':`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("Rocky received Oscar nominations for Best Actor, Best Actress, two Best Supporting Actor, Best Original Screenplay, Best Original Song, and Best Sound.")`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`if movie.lower() == 'rocky iii':`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("Rocky received Oscar an nomination for Best Original Song.")`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`else:`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("{} is not an acceptable entry.".format(awards))`  
   `else:`  
   &nbsp;&nbsp;&nbsp;&nbsp;&nbsp;&nbsp;`print("{} is not an acceptable entry.".format(awards))`
8. For simple cases, it's possible to use a ternary operator to complete a conditional operation in a single line. Ternary operators use the format `name = something if condition else something-else`. _Type and execute:_  
   `reviews = 60`  
   `rating = .93 if reviews > 50 else "Not enough reviews"`  
   `print("On Rotten Tomatoes, Rocky has a rating: {} with a number of reviews: {}.".format(rating * 100, reviews))`
9. Update the [log file](../../log.md) with what you have learned today.

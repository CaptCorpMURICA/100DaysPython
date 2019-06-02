"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module1_day10_ifElse.py
    Creation Date:  6/2/2019, 8:55 AM
    Description:    Learn about conditional programming in python.
"""

# Conditional programming is no different than all of the decisions you make in life. _"If I wake up on time, then I'll
# make breakfast."_ In python, conditional programming takes the form of `if/elif/else`, where the action is indented
# underneath the condition. The action is completed if the condition is true. The end of the conditional statement
# requires a colon (`:`) to mark the end of the line.
lost = True
if lost:
    print("We're going to need a montage.")
# If the primary condition (`if`) is not met, the action is not completed. An `else` statement can be used to ensure a
# specific action is taken if the primary condition is not met.
lost = False
if lost:
    print("We're going to need a montage.")
else:
    print("Celebrate by giving Adrian a kiss.")
# Additional conditions can be added by using the `elif` statement. There is no limit to the number of `elif` statements
# that can be added; however, there can only be a max of one `if` and `else` statement each. Conditions are checked in
# sequential order and the action is completed at the first `True` condition.
prompt = input("What do you want to know? Type: 'steps' for number of steps at the Art Museum, 'bouts' for the major"
               "fights, or 'job' for Rocky's original job.")
if prompt.lower() == "steps":
    print("You need to run up 72 steps to take a picture with Rocky at the Art Museum in Philadelphia.")
elif prompt.lower() == "bouts":
    print("""Rocky (1976): Apollo Creed
    Rocky II (1979): Apollo Creed
    Rocky III (1982): James 'Clubber' Lang
    Rocky IV (1985): Ivan Drago
    Rocky V (1990): Tommy Gunn
    Rocky Balboa (2006): Mason Dixon""")
elif prompt.lower() == "job":
    print("Before becoming a professional boxer, Rocky was nothing but a 'bum' that collected payments for a loan"
          "shark.")
else:
    print("{} is not an acceptable entry.".format(prompt))
# As the number of conditions increases though, the code can begin to become unruly.
num = int(input("Select a positive number between 1 and 10: "))
if num > 10:
    print("How can you expect to be the champ if you can't follow directions?")
elif num < 1:
    print("How can you expect to be the champ if you can't follow directions?")
elif num < 3:
    print("Only {} sides of beef? You need to punch more if you plan to be the champ.".format(num))
elif num < 6:
    print("{} sides of beef? That's a good number to punch if you want to be the champ.".format(num))
elif num < 10:
    print("{} sides of beef? Punching that many is a waste. Even if you become the champ, you shouldn't be "
          "wasteful.".format(num))
else:
    print("Well, that shouldn't have happened. {} caused an error.".format(num))
# In the example above, the message for `3` would make the fourth condition true. Therefore, the program flow would end
    # before reaching subsequent conditions.

# Nested conditional statements are a way to efficiently segment actions based on a parent condition being met first.
awards = input("Which would you like to see, awards won or nominated?")
if awards.lower() == 'won':
    print("Rocky won Oscars for Best Picture, Best Director, and Best Film Editing")
elif awards.lower() == 'nominated':
    movie = input("Which movie do you want to hear about, Rocky or Rocky III?")
    if movie.lower() == 'rocky':
        print("Rocky received Oscar nominations for Best Actor, Best Actress, two Best Supporting Actor, Best Original "
              "Screenplay, Best Original Song, and Best Sound.")
    elif movie.lower() == 'rocky iii':
        print("Rocky received Oscar an nomination for Best Original Song.")
    else:
        print("{} is not an acceptable entry.".format(awards))
else:
    print("{} is not an acceptable entry.".format(awards))
# For simple cases, it's possible to use a ternary operator to complete a conditional operation in a single line.
# Ternary operators use the format `name = something if condition else something-else`.
reviews = 60
rating = .93 if reviews > 50 else "Not enough reviews"
print("On Rotten Tomatoes, Rocky has a rating: {} with a number of reviews: {}.".format(rating * 100, reviews))

#conditional programming takes the form of if/elif/else, the end of a conditional statement requires a colon (:)
lost = True
if lost:
    print("We're going to need a montage.")

#using else ensures a specific action is taken if the primary condition is not met
lost = False
if lost:
    print("We're going to need a montage.")
else:
    print("Celebrate by giving Adrian a kiss.")

#there can only be a max of one if and else statement, but unlimited elif statements
prompt = input("What do you want to know? Type: 'steps' for number of steps at the Art Museum, 'bouts' for the major fights, or 'job' for Rocky's original job.")
if prompt.lower() == "steps":
    print("You need to run up 72 steps to take a picture with Rocky at the Art Museum in Philadelphia.")
elif prompt.lower() == "bouts":
    print("Rocky (1976): Apollo Creed\n Rocky II (1979): Apollo Creed\n Rocky III (1982): James 'Clubber' Lang\n Rocky IV (1985): Ivan Drago\n Rocky V (1990): Tommy Gunn/n Rocky Balboa (2006): Mason Dixon")
elif prompt.lower() == "job":
    print("Before becoming a professional boxer, Rocky was nothing but a 'bum' that collected payments for a loan shark.")
else: 
    print(f"{prompt} is not an acceptable entry.")

#as the number of conditions increases, the code can become unruly
num = int(input("Select a positive number between 1 and 10: "))
if num > 10:
    print("How can you expect to be the champ if you can't follow directions?")
elif num < 1:
    print("How can you expect to be the champ if you can't follow directions")
elif num < 3:
    print(f"Only {num} sides of beef? You need to punch more if you plan to be the champ.")
elif num < 6: 
    print(f"{num} sides of beef? That's a good number to punch if you want to be the champ.")
elif num < 10: 
    print(f"{num} sides of beef? Punching that many is a waste. Even if you become the champ, you shouldn't be wasteful.")
else: 
    print(f"Well, that shouldn't have happened. {num} caused an error.")

#nested conditional statements efficiently segment actions based on a parent condition being met first
awards = input("Which would you like to see, awards won or nominated?")
if awards.lower() == 'won':
    print("Rocky won Oscars for Best Picture, Best Director, and Best Film Editing")
elif awards.lower() == 'nominated': 
    movie = input("Which movie do you want to hear about, Rocky or Rocky III?")
    if movie.lower() == 'rocky':
        print("Rocky received Oscar nominations for Best Actor, Best Actress, two Best Supporting Actor, Best Original Screenplay, Best Original Song, and Best Sound.")
    elif movie.lower() == 'rocky iii': 
        print("Rocky III received an Oscar nomination for Best Original Song.")
    else: print(f"{movie} is not an acceptable entry.")
else: print(f"{awards} is not an acceptable entry.")

# for simple cases, it's possible to use a ternary operator to complete a conditional operation in a single line
reviews = 60
rating = .93 if reviews > 50 else "not enough reviews"

print(f"On Rotten Tomatoes, Rocky has a rating: {rating * 100} with a number of reviews: {reviews}.")
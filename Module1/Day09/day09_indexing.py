#specific items can be retrieved from a list by using its indicies
quotes = ["Pitter patter, let's get ar 'er", "Hard no!", "H'are ya now?", "Good-n-you", "Not so bad.", "Is that what you appreciates about me?"]
print(quotes[0])
print(f"{quotes[2]}\n\t {quotes[3]}\n {quotes[4]}")

#slicing uses the format [start:stop:step], start is inclusive but stop is exclusive
print(quotes[2:5])

#the step can be used to identify how manuy items to skip between returned values
print(quotes[::2])

#the step can also be used to reverse the order of the returned values
print(quotes[::-1])
print("break")

#slicing can be combined with indices to return a sequence from a specific item
print(quotes[0][::2])
print(quotes[0][::-1])

#slicing doesn't only need to applied to lists
wayne = "Toughest Guy in Letterkenny"
print(wayne[::-1])
print("break")

#retrieval by index and slicing can also be applied to a string
print("That's a Texas sized 10-4."[0:9:2])
print("0123456789_acbdef"[0:9:2])

#neither the start, nor the stop values are required when slicing
print(quotes[:])
print(quotes[3:])
print(quotes[:3])
print(quotes[::3])
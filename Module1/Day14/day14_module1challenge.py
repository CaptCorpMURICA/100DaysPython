# Create a program that iterates through a list of values. 
# If the object is immutable, print the type and advance to the next step. 
# If the object is mutable and a string, add "Allegedly" to the end. 
# If the object is mutable and a number, take 10 (for an int) to 20 (for a float) percent off, print the new value, and overwrite the value in the existing position. 
# If an object is not a string, number, or tuple, end the program immediately while displaying the object and the type for review.

content = ["Wayne is the toughest guy in Letterkenny.", list(range(0,101,10)), ("Wayne", "Dan", "Katy", "Daryl"), 10.4]

print(type(content))
print("=" * 26)

# we know that content is a list; for a check, create a for loop to get each element's type
for i in range(len(content)):
    print("Content {}: {}".format(i + 1, type(content[i])))
print("=" * 26)

# loop through each element, determine it's type and iterate the index
for i in range(len(content)):
    if type(content[i]) is tuple:
        print("{} is a {}.".format(content[i], type(content[i])))
        continue
    elif type(content[i]) is str:
        content[i] += " Allegedly."
        print(content[i])
    elif type(content[i]) is list:
        # since we need a further transformation, declare a new list and append the changes to it
        new_list = content[i]
        # we need additional functionality to make the transformation, add a nested for loop
        for j in range(len(new_list)):
            if type(new_list[j]) is int:
                new_list[j] -= new_list[j] * .1
            elif type(new_list[j]) is float:
                new_list[j] -= new_list[j] * .2
                new_list.append(j)
            else:
                break
        # pass the new list back to the index
        content[i] = new_list
        print(content[i])
    elif type(content[i]) is float:
        content[i] -= content[i] * .2
        print(content[i])
    else:
        print("{} is a {} and nothing was done about it".format(content[i], type(content[i])))
        break
"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module1_day14_challenge_soln.py
    Creation Date:  6/2/2019, 8:55 AM
    Description:    Create a program that iterates through a list of values. If the object is immutable, print the type
                    and advance to the next step. If the object is mutable and a string, add "Allegedly" to the end. If
                    the object is mutable and a number, take 10 (for an int) to 20 (for a float) percent off, print the
                    new value, and overwrite the value in the existing position. If an object is not a string, number,
                    or tuple, end the program immediately while displaying the object and the type for review.
"""

content = ["Wayne is the toughest guy in Letterkenny.", list(range(0, 101, 10)), ("Wayne", "Dan", "Katy", "Daryl"),
           10.4]

for i in range(0, len(content)):
    if type(content[i]) is tuple:
        print("{} is a {}".format(content[i], type(content[i])))
        continue
    elif type(content[i]) is str:
        content[i] += " Allegedly."
        print(content[i])
        continue
    elif type(content[i]) is list:
        updated_list = content[i]
        for j in range(0, len(updated_list)):
            if type(updated_list[j]) is int:
                updated_list[j] -= updated_list[j] * .1
            elif type(updated_list[j]) is float:
                updated_list[j] -= updated_list[j] * .2
                updated_list.append(j)
            else:
                updated_list.append(j)
        content[i] = updated_list
        print(content[i])
    elif type(content[i]) is int:
        content[i] -= content[i] * .1
        print(content[i])
    elif type(content[i]) is float:
        content[i] -= content[i] * .2
        print(content[i])
    else:
        print("{} is a {}, and nothing was done about it.".format(content[i], type(content[i])))
        break

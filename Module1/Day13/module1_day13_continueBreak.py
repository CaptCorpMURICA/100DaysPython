"""
    Author:         CaptCorpMURICA
    Project:        100DaysPython
    File:           module1_day13_continueBreak.py
    Creation Date:  6/2/2019, 8:55 AM
    Description:    Learn about continue/break operations in python.
"""

# Print only consonants from a given text.
motivation = "Over? Did you say 'over'? Nothing is over until we decide it is! Was it over when the Germans bombed " \
             "Pearl Harbor? Hell no! And it ain't over now. 'Cause when the goin' gets tough...the tough get goin'! " \
             "Who's with me? Let's go!"
output = ""
for letter in motivation:
    if letter.lower() in 'bcdfghjklmnpqrstvwxyz':
        output += letter
print(output)

#  However, this example can also be completed by using a continue action. If the condition is met, then the continue
#  advances the program to the next stage.
motivation = "Over? Did you say 'over'? Nothing is over until we decide it is! Was it over when the Germans bombed " \
             "Pearl Harbor? Hell no! And it ain't over now. 'Cause when the goin' gets tough...the tough get goin'! " \
             "Who's with me? Let's go!"
output = ""
for letter in motivation:
    if letter.lower() not in 'bcdfghjklmnpqrstvwxyz':
        continue
    else:
        output += letter
print(output)

# Conversely, the break action halts the program when the condition is met. For instance, what if we wanted to display
# all of the letters until the first instance of a non-letter? A `break` can be used to end the loop once the condition
# is met. _Type and execute:_
motivation = "Over? Did you say 'over'? Nothing is over until we decide it is! Was it over when the Germans bombed " \
             "Pearl Harbor? Hell no! And it ain't over now. 'Cause when the goin' gets tough...the tough get goin'! " \
             "Who's with me? Let's go!"
output = ""
for letter in motivation:
    if letter.lower() not in 'abcdefghijklmnopqrstuvwxyz':
        output += letter
    else:
        break
print(output)

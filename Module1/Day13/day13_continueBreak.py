#print only constants from a given text
motivation = "Over? Did you say 'over'? Nothing is over until we decide it is! Was it over when the Germans bombed Pearl Harbor? Hell no! And it ain't over now. 'Cause when the goin' gets tough...the tough get goin'! Who's with me? Let's go!"
output = ""

print(output)
for letter in motivation:
    if letter.lower() in 'bcdfghjklmnpqrstvwxyz':
        output += letter
print(output)

#however, this example can also be completed using a continue action
motivation = "Over? Did you say 'over'? Nothing is over until we decide it is! Was it over when the Germans bombed Pearl Harbor? Hell no! And it ain't over now. 'Cause when the goin' gets tough...the tough get goin'! Who's with me? Let's go!"
output = ""

for letter in motivation:
    if letter.lower() not in 'bcdfghjklmnpqrstvwxyz':
        continue
    else:
        output += letter
print(output)

#conversly, the break action halts the prgram wgen the condition is met
motivation = "Over? Did you say 'over'? Nothing is over until we decide it is! Was it over when the Germans bombed Pearl Harbor? Hell no! And it ain't over now. 'Cause when the goin' gets tough...the tough get goin'! Who's with me? Let's go!"
output = ""

for letter in motivation:
    if letter.lower() not in 'abcdefghijklmnopqrstuvwxyz':
        output += letter
    else:
        break
print(output)
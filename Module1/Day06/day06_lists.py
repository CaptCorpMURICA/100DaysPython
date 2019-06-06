#creating an empty list
list_1 = []
list_2 = list()

print("List 1 Type: {}\nList 2 Type: {}".format(type(list_1), type(list_2)))
print("break")
print(f"List 1 Type: {type(list_1)}\nList 2 Type: {type(list_2)}")

#list function created a list where each character is a seperate entry
text = "Luggage Combination"

print(list(text))

#.sort() method is used to sort a list
luggage = [1, 3, 5, 2, 4]
luggage.sort()

print(luggage)

#if a sort is applied to a variable created from a list, the sort is also applied to the original 
numbers = [1, 2, 3, 4, 5]
numbers_sorted = numbers
numbers_sorted.sort(reverse=True)

print(f"numbers: {numbers}\n numbers_sorted: {numbers_sorted}")

#in order to create a new version, a function needs to be called to the original list
numbers = [1, 2, 3, 4, 5]
numbers_sorted = list(numbers)
numbers_sorted.sort(reverse=True)

print(f"numbers: {numbers}\n numbers_sorted: {numbers_sorted}")

#lists are easily combined 
odd = [1, 3, 5]
even = [2, 4]
luggage = odd + even

print(luggage)

luggage = [1, 3, 5]
even = [2,4]
luggage.extend(even)

print(luggage)
print(f"Unsorted list: {luggage}")
print(f"Using the sorted() function: {sorted(luggage)}")

luggage.sort()

print(f"Using the .sort() method: {luggage}")

#items can be added by also using the .append() method
lines = []
lines.append("They told me to comb the desert, so I'm combing the desert")
lines.append("YOGURT! I hate Yogurt! Even with strawberries")
lines.append("We'll meet again Spaceballs 2: The Quest for More Money")

print(lines)

#the index of a requested item can be obtained using the .index() method, use the count method to obtain frequency of an iteam
luggage = [1, 2, 3, 4, 5]

print(luggage.index(2))

quote = list("YOGURT! I hate Yogurt! Even with strawberries")
print(quote.count("r"))

#using the .insert(index, item) method can be used to add a new item to the list at a specific position
luggage = [1, 2, 4, 5]
luggage.insert(2, 3)

print(luggage)

#the .pop(i) method is used to remove and return the final element, or from a specific index i
luggage = [1, 2, 3, 3, 4, 5, 6]
luggage.pop()

print(luggage)

luggage.pop(2)
print(luggage)

#the .remove(i) method eliminates a specific item (i) from the list
rng = list(range(1,13))
rng.remove(7)

print(rng)

#the .reverse() method reverses the order of the items
countdown = [5, 4, 3, 2, 1]
countdown.reverse()

print(countdown)

#python can conduct transformations to a list while declaring a new list
sample = list(range(1,13))
times_12 = [i * 12 for i in sample]

print(times_12)

#a list can be cleared 
luggage.clear()

print(luggage)

#since lists are mutable, items can be changed
luggage = [2, 2, 3, 4, 5]
luggage[0] = 1

print(luggage)
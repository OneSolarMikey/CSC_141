# Following PEP 8 guidelines.

"""
1) Four spaces for each indentation
2) 80 characters in each line
3) NO excessive blank lines
"""

# List of pizzas.

fav_pizzas = ['cheesesteak', 'buffalo', 'white']
for pizza in fav_pizzas:
    print(pizza)

# Printing a sentence with each element in the for loop.
for pizza in fav_pizzas:
    print(f"I like {pizza} pizza!\n")

# Printing outside of the for loop.
print("I really like pizza!")

# Slicing elements in a list.

fav_pizzas = ['cheesesteak', 'buffalo', 'white', 'chicken bacon ranch', 'margarita']

# Printing the first three items in a list.
print("The first three items in the list are:")
for pizza in fav_pizzas[0:3]:
    print(pizza)

# Printing in the middle of a list.
print("\nThree items from the middle of the list are:")
for pizza in fav_pizzas[1:4]:
    print(pizza)

# Printing the last three items in a list.
print("\nThe last three items in the list are:")
for pizza in fav_pizzas[2:6]:
    print(pizza)

# Copying lists.

fav_pizzas = ['cheesesteak', 'buffalo', 'white']
friends_pizzas = fav_pizzas[:]

fav_pizzas.append('chicken bacon ranch')
friends_pizzas.append('hawaiian')

print("\nMy favorite pizzas are:")
for pizza in fav_pizzas:
    print(pizza)

print("\nMy friends favorite pizzas are:")
for pizza in friends_pizzas:
    print(pizza)
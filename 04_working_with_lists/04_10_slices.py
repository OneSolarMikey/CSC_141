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
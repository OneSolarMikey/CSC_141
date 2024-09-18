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
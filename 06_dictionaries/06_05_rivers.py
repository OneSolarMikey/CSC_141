# Printing through dictionaries with loops.

famous_rivers = {
    'amazon': 'brazil', 
    'mississippi': 'united states', 
    'yangtze': 'china'
    }

for river, country in famous_rivers.items(): # for key, value in dictionary.items()
    print(f"The {river.title()} flows through {country.title()}.")
print('\n')

# Printing each key in a dictionary with .keys()
for river in famous_rivers.keys():
    print(river.title())
print('\n')

# Printing each value in a dictionary with .values()
for country in famous_rivers.values():
    print(country.title())

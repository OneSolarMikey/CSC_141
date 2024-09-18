# Lists that cannot change are "tuples".

buffet_menu = ('chicken', 'rice', 'corn', 'beans', 'potatoes')
print('Original menu')
for food in buffet_menu:
    print(food)

# Cannot modify tuples.
#buffet_menu[0] = 'turkey'

"""
line 7, in <module>
    buffet_menu[0] = 'turkey'
    ~~~~~~~~~~~^^^
TypeError: 'tuple' object does not support item assignment
"""

# Rewriting tuples.
buffet_menu = ('steak', 'rice', 'corn', 'bread rolls', 'potatoes')
print('\nUpdated menu')
for food in buffet_menu:
    print(food)
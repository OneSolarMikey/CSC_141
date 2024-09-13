## Using every function for lists.

# Printing specific elements in a list.
shoe_types = ['nike', 'reebok', 'adidas', 'under armour', 'puma']
print(shoe_types[0].title())
print(shoe_types)
print('\n')

# Replacing elements in a list.
shoe_types[4] = 'new balance'
print(shoe_types)
print('\n')

# Adding elements to a list with "append()."
shoe_types.append('brooks')
print(shoe_types)
print('\n')

# Adding elements to a list with "inset()."
shoe_types.insert(1, 'asics')
print(shoe_types)
print('\n')

# Removing elements from a list using "del" statement.
del shoe_types[2]
print(shoe_types)
print('\n')

# Removing elements from a statement using "pop()."
popped_shoe = shoe_types.pop(1)
print(shoe_types)
print('\n')

# Removing elements from a list with it's value.
shoe_types.remove('under armour')
print(shoe_types)
print('\n')

# Printing a list alphabetically using "sorted()."
print(sorted(shoe_types))
print(shoe_types)
print('\n')

# Printing a list in reverse 
print(shoe_types)
shoe_types.reverse()
print(shoe_types)
print('\n')

# Permanently sorting a list with "sort()."
print(shoe_types)
shoe_types.sort()
print(shoe_types)
print('\n')

# Finding how many elements are in a list.
message = len(shoe_types)
print(message)
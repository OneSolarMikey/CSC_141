# Organizing Lists.

travel_list = ['Switzerland', 'Australia', 'Ireland', 'Spain', 'Italy']
print(travel_list)
print('\n')

# Printing the list in alphabetical order temporarily with "sorted()"".
print(sorted(travel_list))
print(travel_list)
print('\n')

# Printing the list in reversve alphabetically.
reverse_list = sorted(travel_list, reverse = True)
print(reverse_list)
print(travel_list)
print('\n')

# Printing the list in reverse order with "reverse()".
travel_list.reverse()
print(travel_list)
travel_list.reverse()
print(travel_list)
print('\n')

# Sorting a list permanently with "sort()".
travel_list.sort()
print(travel_list)
travel_list.sort(reverse = True)
print(travel_list)
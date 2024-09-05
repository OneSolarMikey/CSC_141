# Stripping whitespace.

name = "  \n\t   Kenny Wolf  \n\n   "
# This will remove the whitespace from the left of the name.
print(name.lstrip())

# This will remove the whitespace form the right of the name.
print(name.rstrip())

# This will remove the whitespace from both sides of the name
print(name.strip())

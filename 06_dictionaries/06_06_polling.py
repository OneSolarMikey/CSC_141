# if else statements in dictionaries

favorite_languages = {
    'jen': 'python',
    'sarah': 'c',
    'edward': 'rust',
    'phil': 'python',
    }

poll = ['kenny', 'jen', 'sarah', 'carter', 'edward', 'phil']

# Printing special statements if a name is not in the dictionary
for name in poll:
    if name in favorite_languages:
        print(f"Thank you {name.title()}, you have already taken the poll.")
    else:
        print(f"{name.title()}, you need to take the poll.")
# Using an empty list.

usernames = []

for name in usernames:
        if name == 'admin':
                print(f'Hello {name}, would you like to see a status report?')
        else:
                print(f'Welcome {name}.')
else:
    print('We need to find some users!')
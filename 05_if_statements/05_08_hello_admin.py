# Looping through lists with if.

usernames = ['admin', 'Kenny', 'Carter', 'Preston', 'Michael', 'Tommy']

for name in usernames:
        if name == 'admin':
                print(f'Hello {name}, would you like to see a status report?')
        else:
                print(f'Welcome {name}.')
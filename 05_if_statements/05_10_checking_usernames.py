# Comparing lists

current_users = ['Kenny', 'Carter', 'Preston', 'Michael', 'Mac']
new_users = ['Alyssa', 'Alexis', 'Carter', 'Caroline', 'Mac']

for new_user in new_users:
    if new_user in current_users:
        print(f"Please pick a new username other than {new_user}.")
    else:
        print(f"This username, {new_user} is available.")
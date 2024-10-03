# Dictionaries inside lists.

user_1 = {
    'first_name': 'Kenny', 
    'last_name': 'Kerby', 
    'age': 22, 
    'city': 'Pottsville',
    }

user_2 = {
    'first_name': 'Carter',
    'last_name': 'Wolf',
    'age': 47,
    'city': 'Lancaster'
    }

user_3 = {
    'first_name': 'Preston', 
    'last_name': 'Smithman', 
    'age': 60, 
    'city': 'Pittsburgh',
    }

people = [user_1, user_2, user_3]

# for looping through the list that contains dictionaries
for user in people:
    full_name = f"{user['first_name']} {user['last_name']}"
    age = user['age']
    city = user['city']

    print(full_name)
    print(age)
    print(city)
# Dictionaries inside lists

pet_1 = {
    'animal': 'turtle',
    'owner': 'Kenneth'
    }
pet_2 = {
    'animal': 'cat',
    'owner': 'Elissa',
    }
pet_3 = {
    'animal': 'rabbit',
    'owner': 'Lionel',
    }

pets = [pet_1, pet_2, pet_3]

for pet in pets:
    kop = pet['animal'] # kop = kind of pet
    owner = pet['owner']
    print(f"{owner} has a pet {kop}")

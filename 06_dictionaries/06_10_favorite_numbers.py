# Lists inside dictionaries

fav_num = {
    'Kenny': [23, 45], 
    'Carter': [7, 8, 9],
    'Alyssa': [6, 10,],
    'Preston': [46, 356],
    'Mac': [10, 55, 66],
    }

for name, numbers in fav_num.items():
    print(f"{name}'s favortie numbers are:")
    for number in numbers:
        print(f"{number}")
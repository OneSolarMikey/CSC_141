# Lists inside dictionaries

favorite_places = {
    'Kenny':['Rio', 'Atlanta'],
    'Carter': ['Denmark', 'Sweeden'],
    'Preston':['Madrid', 'Dublin'],
    }

for name, places in favorite_places.items():
    print(f"{name}'s favorite places to visit are:")
    for place in places:
        print(f"{place}")
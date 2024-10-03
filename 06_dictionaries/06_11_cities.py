# Dictionaries inside dictionaries

cities = {
    'Atlanta': {
        'country': 'United States',
        'population': '498.72k',
        'fact': 'The capital city of Georgia'
    },
    'Dublin': {
        'country': 'Ireland',
        'population': '592.71k',
        'fact': 'The name comes from an old Celtic name meaning "Black Pool"'
    },
    'Tokyo': {
        'country': 'Japan',
        'population': '14.19 million',
        'fact': 'The largest city in the world'
    }
}

for city, info in cities.items():
    print(f"\nInformation about {city}:")
    location = f'{info['country']}'
    pop = f'{info['population']}'
    fact = f'{info['fact']}'

    print(f"\tLocated in {location}")
    print(f"\tWith a population of {pop}")
    print(f"\t{fact}")
    
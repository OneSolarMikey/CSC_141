# 

def city_country(city_name, country_name):
    '''Cities and what country they are in'''
    place = f"{city_name}, {country_name}"
    return place.title()

formatted_name = city_country('paris', 'france')
print(formatted_name)
formatted_name = city_country('moscow', 'russia')
print(formatted_name)
formatted_name = city_country('berlin', 'germany')
print(formatted_name)
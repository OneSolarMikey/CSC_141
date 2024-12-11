# More arguments with functions

def describe_city(name, country = 'Ireland'):
    '''Cities inside countries'''
    print(f"{name.title()} is in {country.title()}.")

describe_city('dublin')
describe_city('belfast')
describe_city('rome', 'italy')
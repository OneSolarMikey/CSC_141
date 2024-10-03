# Looping through a dictionary.

definition = {
    'tuple': "A list where it's value cannot change",
    'variable': "Every one is connected to a value in which information is stored",
    'string':"A series of characters inside quotes",
    'for loop':"Used to loop through a list",
    'dictionary':"A collection of key-value pairs",
    'conditional test':"Uses values True and False to decide whether the code in an if statement should be executed",
    'functions':"Named blocks of code that perform a specific task and ran whenever they are needed",
    'comment':"Allows notes to be written within programs",
    'constant':"A variable whose value stays the same throughout the program",
    'syntax error':"When code is not recognized in a section of the program",
    }

for name, meaning in definition.items(): # for key, value in dictionary.items():
    print(f"\n{name.title()}: {meaning}.")
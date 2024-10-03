# Adding extra to favorite_languages.py page 109

favorite_languages = {
    'jen': ['python', 'rust'],
    'sarah': ['c'],
    'edward': ['rust', 'go'],
    'phil': ['python', 'haskell'],
    'howard': ['r', 'java'],
    'linda': ['c sharp'],
    }

for name, languages in favorite_languages.items():
    print(f"\n{name.title()}'s favorite languages are:")
    for language in languages:
        print(language.title())
        if language == 'python':
            print("They can't handle the unlimited power!")
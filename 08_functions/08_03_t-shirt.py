# Different arguments in functions

def make_shirt(size, text):
    '''Making t-shirts'''
    print(f"Make a {size} shirt that says {text}.")

make_shirt('small', 'Go Lions') # Positional Arguments
make_shirt(text = 'Go Lions', size = 'small') # Keyword Arguments
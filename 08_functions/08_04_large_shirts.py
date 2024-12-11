# More arguments with funtions

def make_shirt(size = 'large', text = 'I love Python'):
    '''Making unique t-shirts'''
    print(f"Make a {size} shirt that says {text}.")

make_shirt()
make_shirt(size = 'medium')
make_shirt(size = 'small', text = 'I love HTML')
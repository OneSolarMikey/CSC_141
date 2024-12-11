#

def sandwich(*items):
    '''Items being asked for on a sandwich'''
    print("Your sandwich includes:")
    for item in items:
        print(f"- {item}")

sandwich('turkey')

sandwich('ham', 'cheese')

sandwich('bacon', 'lettuce', 'tomato')
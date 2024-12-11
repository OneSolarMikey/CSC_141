# More while loops with try abd except blocks

while True:
    age_input = input("Please enter your age (or type 'quit' to quit): ")

    if age_input.lower() == 'quit':
        print("Exiting the program.")
        break
    
    try:
        age = int(age_input)
        
        if age < 3:
            print("Your ticket is free!")
        elif 3 <= age <= 12:
            print("Your ticket costs $10.")
        else:
            print("Your ticket costs $15.")
    except ValueError:
        print("Please enter a valid age or type 'quit' to quit.")

# Three ways to exit a loop

prompt = "\nSelected pizza toppings:"
prompt += "\n(Enter 'quit' when you are finished.)"

# The loop runs until 'quit' is entered
toppings = ""
while toppings.lower() != 'quit':
    toppings = input(prompt)

    if toppings.lower() == 'quit':
        break
    else:
        print(f"Adding {toppings.title()} to pizza.")


# Initialize an active variable to control the loop
active = True

prompt = "\nSelected pizza toppings:"
prompt += "\n(Enter 'quit' when you are finished.)"

while active:
    toppings = input(prompt)

    if toppings.lower() == 'quit':
        active = False
    else:
        print(f"Adding {toppings.title()} to pizza.")


prompt = "\nSelected pizza toppings:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    toppings = input(prompt)

    if toppings.lower() == 'quit':
        # Exit the loop using break
        break
    else:
        print(f"Adding {toppings.title()} to pizza.")

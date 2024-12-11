# Using while loops

prompt = "\nSelected pizza toppings:"
prompt += "\n(Enter 'quit' when you are finished.)"

while True:
    toppings = input(prompt)

    if toppings == 'quit':
        break
    else:
        print(f"Adding {toppings.title()} to pizza.")
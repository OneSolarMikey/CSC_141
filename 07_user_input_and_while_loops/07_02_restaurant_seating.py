# Asking for user input() involving numbers

number = input("How many people are in your dinner group for tonight?")
number = int(number)

if number > 8:
    print(f"\nSorry, but you will have to wait for a table.")
else:
    print(f"\nWe have a table ready for you!")
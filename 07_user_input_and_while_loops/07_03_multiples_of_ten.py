# Using the Modulo Operator (%)

number = input("Enter any number and we will find out if it is a multiple of 10.")
number = int(number)

if number % 10 == 0:
    print(f"{number} is a multiple of ten.")
else:
    print(f"{number} is not a multiple of ten.")
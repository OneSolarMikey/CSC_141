# More if-elif-else.

age = 21

if age < 2:
    print("The person is a baby.")
elif 2 <= age < 4:
    print("The person is a toddler.")
elif 4 <= age < 13:
    print("The person is a kid.")
elif 13 <= age < 20:
    print("The person is a teenager.")
elif 20 <= age < 65:
    print("The person is an adult.")
else:
    print("The person is an elder.")
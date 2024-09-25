# Different conditional tests.

# Tests for equality and inequality with strings.
flower1 = "Rose"
flower2 = "rose"

# True and False examples.
print(flower1 == "Rose")
print(flower1 != "Rose")

# Tests using the lower() method.
print(flower1.lower() == flower2)
print(flower1.lower() == "Hello")

# Numerical tests involving equality and inequality, greater than and less than, greater than or equal to, and less than or equal to.
number1 = 10
number2 = 20

# True and False examples.
print(number1 < number2)
print(number1 >= number2)

# Tests using the and keyword and the or keyword.
age = 25

# True and False examples.
print(age > 18 and age < 30)
print(age < 18 or age > 30)

# Test whether an item is in a list.
fruits = ["apple", "banana", "cherry"]

# True and False examples.
print("banana" in fruits)
print("grape" in fruits)

# Test whether an item is not in a list.
print("grape" not in fruits)
print("banana" not in fruits)

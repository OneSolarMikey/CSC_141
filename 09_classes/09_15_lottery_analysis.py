import random

# Create a list containing 10 numbers and 5 letters
items = [1, 2, 3, 4, 5, 6, 7, 8, 9, 0, 'A', 'B', 'C', 'D', 'E']

# Define your lottery ticket with 4 random selections
my_ticket = random.sample(items, 4)
print(f"My ticket numbers/letters: {my_ticket}")

# Initialize a counter for the number of attempts
attempts = 0

# Loop until a winning ticket is found
while True:
    # Randomly select 4 items for the winning ticket
    winning_selection = random.sample(items, 4)
    attempts += 1  # Increment the attempts counter
    
    # Check if the winning selection matches your ticket
    if set(winning_selection) == set(my_ticket):
        break  # Exit the loop if you have a winning ticket

# Print the number of attempts it took to win
print(f"It took {attempts} attempts to win with the ticket: {winning_selection}")

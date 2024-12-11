# die.py

import random

class Die:
    def __init__(self, sides=6):
        """Initialize the die with a number of sides."""
        self.sides = sides

    def roll_die(self):
        """Roll the die and return a random number between 1 and the number of sides."""
        return random.randint(1, self.sides)

# Function to roll the die multiple times and print the results
def roll_multiple_times(die, rolls=10):
    results = []
    for _ in range(rolls):
        result = die.roll_die()
        results.append(result)
    return results

##### main.py

from die import Die, roll_multiple_times  # Import the Die class and the rolling function

# Create a 6-sided die and roll it 10 times
six_sided_die = Die()
print("Rolling a 6-sided die 10 times:")
six_sided_results = roll_multiple_times(six_sided_die)
print(six_sided_results)

# Create a 10-sided die and roll it 10 times
ten_sided_die = Die(sides=10)
print("\nRolling a 10-sided die 10 times:")
ten_sided_results = roll_multiple_times(ten_sided_die)
print(ten_sided_results)

# Create a 20-sided die and roll it 10 times
twenty_sided_die = Die(sides=20)
print("\nRolling a 20-sided die 10 times:")
twenty_sided_results = roll_multiple_times(twenty_sided_die)
print(twenty_sided_results)

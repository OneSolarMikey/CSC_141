# Filling with user input

vacation_poll = {}

while True:
    name = input("What is your name? (Type 'quit' to end the poll): ")
    
    if name.lower() == 'quit':
        break
    
    vacation_destination = input(f"If you could visit one place in the world, where would you go, {name}? ")
    
    vacation_poll[name] = vacation_destination

print("\n--- Vacation Poll Results ---")
for name, destination in vacation_poll.items():
    print(f"{name} would like to visit {destination}.")

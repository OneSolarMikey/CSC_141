## Making a guest list.

guest_list = ['Kenny', 'Carter', 'Preston']

# Printing a message to the first name on the list.
message = f"I'm having a dinner later in the week and I would like you to be there {guest_list[0]}."
print(message)

# Printing a message to the second name on the list.
message = f"\nI'm having a dinner later in the week and I would like you to be there {guest_list[1]}."
print(message)

# Printing a message to the third name on the list.
message = f"\nI'm having a dinner later in the week and I would like you to be there {guest_list[2]}."
print(message)

## Modifying lists.

message = f"\n{guest_list[2]} cannot make the dinner."
print(message)

# Changing a name in the list.
guest_list[2] = 'Tommy'

# Printing a message to the first name in the list.
message = f"\nI'm having a dinner later in the week and I would like you to be there {guest_list[0]}."
print(message)

# Printing a message to the second name in the list.
message = f"\nI'm having a dinner later in the week and I would like you to be there {guest_list[1]}."
print(message)

# Printing a message to the new third name in the list.
message = f"\nI'm having a dinner later in the week and I would like you to be there {guest_list[2]}."
print(message)
#

messages = [
    "Hey, what's up!",
    "How are you?",
    "Talk to you later."
    ]

sent_messages = []


def send_messages(messages, sent_messages):
    while messages:
        current_message = messages.pop(0)
        print(current_message)
        sent_messages.append(current_message)

send_messages(messages[:], sent_messages) 

print("\nMessages:", messages)
print("Sent Messages:", sent_messages)
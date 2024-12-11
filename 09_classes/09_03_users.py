class User:
    def __init__(self, first_name, last_name, age, email, location):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age
        self.email = email
        self.location = location

    def describe_user(self):
        print(f"User Profile:")
        print(f"Name: {self.first_name} {self.last_name}")
        print(f"Age: {self.age}")
        print(f"Email: {self.email}")
        print(f"Location: {self.location}\n")

    def greet_user(self):
        print(f"Hello, {self.first_name} {self.last_name}! Welcome back!\n")


# Create several instances of the User class
user1 = User("Alice", "Johnson", 28, "alice.johnson@example.com", "New York")
user2 = User("Bob", "Smith", 34, "bob.smith@example.com", "Los Angeles")
user3 = User("Charlie", "Davis", 22, "charlie.davis@example.com", "Chicago")

# Call describe_user() and greet_user() for each user
user1.describe_user()
user1.greet_user()

user2.describe_user()
user2.greet_user()

user3.describe_user()
user3.greet_user()

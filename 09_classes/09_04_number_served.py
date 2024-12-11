class Restaurant:
    def __init__(self, restaurant_name, cuisine_type):
        self.restaurant_name = restaurant_name
        self.cuisine_type = cuisine_type
        self.number_served = 0  # Default value for number_served

    def describe_restaurant(self):
        print(f"Restaurant Name: {self.restaurant_name}")
        print(f"Cuisine Type: {self.cuisine_type}")

    def open_restaurant(self):
        print(f"{self.restaurant_name} is now open!")

    def set_number_served(self, number):
        self.number_served = number

    def increment_number_served(self, number):
        self.number_served += number

# Create an instance of the Restaurant class
restaurant = Restaurant("The Gourmet Kitchen", "Italian")

# Print the number of customers served
print(f"Number of customers served: {restaurant.number_served}")

# Change the value of number_served and print it again
restaurant.number_served = 15
print(f"Number of customers served after update: {restaurant.number_served}")

# Use the set_number_served method to set a new number
restaurant.set_number_served(50)
print(f"Number of customers served after using set_number_served: {restaurant.number_served}")

# Use the increment_number_served method to add customers served
restaurant.increment_number_served(20)
print(f"Number of customers served after increment: {restaurant.number_served}")

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


class IceCreamStand(Restaurant):
    def __init__(self, restaurant_name, cuisine_type):
        super().__init__(restaurant_name, cuisine_type)
        self.flavors = []  # List to store ice cream flavors

    def add_flavor(self, flavor):
        self.flavors.append(flavor)

    def display_flavors(self):
        print(f"Available flavors at {self.restaurant_name}:")
        for flavor in self.flavors:
            print(f"- {flavor}")


# Create an instance of IceCreamStand
ice_cream_stand = IceCreamStand("Cool Treats", "Dessert")

# Add some flavors
ice_cream_stand.add_flavor("Vanilla")
ice_cream_stand.add_flavor("Chocolate")
ice_cream_stand.add_flavor("Strawberry")
ice_cream_stand.add_flavor("Mint Chocolate Chip")

# Display the flavors
ice_cream_stand.display_flavors()

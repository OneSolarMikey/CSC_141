class Battery:
    def __init__(self, battery_size=50):
        self.battery_size = battery_size  # Default battery size is 50 kWh

    def get_range(self):
        """Return the range of the battery based on its size."""
        if self.battery_size == 65:
            range = 270  # Range in miles for 65 kWh battery
        else:
            range = 210  # Range in miles for 50 kWh battery
        return range

    def upgrade_battery(self):
        """Upgrade the battery size to 65 kWh if it is not already upgraded."""
        if self.battery_size < 65:
            self.battery_size = 65
            print("Battery upgraded to 65 kWh.")
        else:
            print("Battery is already at 65 kWh.")


class ElectricCar:
    def __init__(self, make, model, year):
        self.make = make
        self.model = model
        self.year = year
        self.battery = Battery()  # Initialize with a default battery

    def describe_car(self):
        """Return a neatly formatted descriptive name for the car."""
        return f"{self.year} {self.make} {self.model}"

    def get_range(self):
        """Return the range of the car based on the battery size."""
        return self.battery.get_range()


# Create an instance of ElectricCar
my_electric_car = ElectricCar("Tesla", "Model 3", 2022)

# Call get_range() to see the initial range
initial_range = my_electric_car.get_range()
print(f"Initial range: {initial_range} miles.")

# Upgrade the battery
my_electric_car.battery.upgrade_battery()

# Call get_range() again to see the upgraded range
upgraded_range = my_electric_car.get_range()
print(f"Upgraded range: {upgraded_range} miles.")

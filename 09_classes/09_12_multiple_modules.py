# main.py

from admin import Admin  # Import Admin class from admin module

# Create an instance of Admin
admin_user = Admin("Alice", "Smith", 30, "alice.smith@example.com", "New York")

# Call the show_privileges method to show that everything is working
admin_user.privileges.show_privileges()

# An AI tool wrote these three functions for the pizza app.
# They run, but each one breaks a requirement. Fix them.

def delivery_fee(food_total):
    # Requirement: delivery costs 3. It is free when the food total is 20 or more.
    if food_total > 20:
        return 0
    return 3


def valid_quantity(quantity):
    # Requirement: a customer may order from 1 to 10 of the same pizza.
    return 1 < quantity < 10


def display_name(name):
    # Requirement: show the name with only the first letter in capitals.
    # For "aisha" give back "Aisha".
    return name.upper()

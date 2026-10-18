PRICES = {"tea": 1.2, "coffee": 2.5, "cake": 3.0}


def average_of_three(a, b, c):
    # Give back the average of the three marks. This has a bug. Fix it.
    return a + b + c / 3


def to_fahrenheit(celsius):
    # Celsius times 9, divided by 5, plus 32. This has a bug. Fix it.
    return celsius * 9 / (5 + 32)


def safe_share(total, people):
    # Share a bill between people. Give back total divided by people.
    # If people is 0, give back 0 and do not divide.
    return None


def price_of(item):
    # Look the item up in the PRICES dictionary.
    # If it is not there, give back 0.0.
    return None


def first_full_marks(scores):
    # Give back the position (starting at 0) of the first score that is 100.
    # Stop as soon as you find it. If there is none, give back -1.
    return None

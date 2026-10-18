def is_teenager(age):
    # A teenager is 13 to 19 years old, including 13 and 19.
    return age > 13 and age < 19


def average_of_two(a, b):
    # Add the two numbers, then divide by 2.
    return a + b / 2


def is_even(number):
    # Even numbers leave no remainder when divided by 2.
    return number // 2 == 0


def age_ok(age):
    # The age must be exactly 15 or exactly 16.
    return age == 15 or 16

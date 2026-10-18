def is_teenager(age):
    # A teenager is 13 to 19 years old. Both 13 and 19 count.
    # This code has a bug. Find it and fix it.
    if age > 13 and age < 19:
        return True
    return False


def count_evens(numbers):
    # Count how many numbers in the list are even.
    # This code has a bug. Find it and fix it.
    count = 0
    for number in numbers:
        count = 0
        if number % 2 == 0:
            count = count + 1
    return count


def sum_to(n):
    # Add the numbers from 1 up to and including n.
    # This code has a bug. Find it and fix it.
    total = 0
    for i in range(n):
        total = total + i
    return total


def countdown(n):
    # Write this one yourself with a while loop.
    # Give back a list that counts down from n to 1.
    # For n = 3 the list is [3, 2, 1].
    return []

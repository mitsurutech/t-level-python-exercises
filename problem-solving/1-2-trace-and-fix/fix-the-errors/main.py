def average(a, b):
    # The average of two numbers: add them, then divide by 2.
    return a + b / 2


def is_adult(age):
    # An adult is 18 or over.
    return age > 18


def total_to(n):
    # Add the whole numbers from 1 up to n. total_to(4) is 1+2+3+4 = 10.
    total = 0
    for number in range(1, n):
        total = total + number
    return total

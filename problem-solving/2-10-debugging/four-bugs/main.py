def average(numbers):
    # Give back the average of the numbers. This has a bug. Find it and fix it.
    total = 0
    for number in numbers:
        total = total + number
    return total / (len(numbers) + 1)


def longest_word(words):
    # Give back the longest word in the list. This has a bug. Find it and fix it.
    longest = ""
    for word in words:
        if len(word) < len(longest):
            longest = word
    return longest


def count_vowels(text):
    # Count the vowels a, e, i, o, u in the text, capital letters too.
    # This has a bug. Find it and fix it.
    count = 0
    for letter in text:
        if letter in "aeiou":
            count = count + 1
    return count


def is_leap_year(year):
    # A leap year is divisible by 4, except years divisible by 100,
    # unless they are also divisible by 400. So 2024 and 2000 are leap years, 1900 is not.
    # This has a bug. Find it and fix it.
    if year % 4 == 0 and year % 100 != 0:
        return True
    return False

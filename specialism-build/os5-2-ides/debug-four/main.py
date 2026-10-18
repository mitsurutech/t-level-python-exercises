def running_total(prices):
    # [2, 3, 4] must give back [2, 5, 9].
    return prices


def count_vowels(text):
    # Count a, e, i, o, u in any case. "Education" has 5.
    count = 0
    for letter in text:
        if letter == "a":
            count = count + 1
    return count


def last_word(text):
    # "the bus is late" must give back "late".
    return text.split()[1]


def first_negative(numbers):
    # Give back the position of the first number below 0, or -1 if there is none.
    for position in range(1, len(numbers)):
        if numbers[position] < 0:
            return position
    return -1

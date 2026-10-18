# Choose test data for any range from low to high (both ends are allowed).
# Give back the data. Do not check it: just choose it.

def normal_value(low, high):
    # A value that is clearly inside the range, not on an edge.
    return 0


def valid_extreme(low, high):
    # A list of the two values on the very edges that are still allowed.
    return []


def invalid_extreme(low, high):
    # A list of the two values just outside the edges, one on each side.
    return []


def erroneous_examples():
    # A list of at least three values that are not whole numbers at all,
    # such as text. Do not use numbers.
    return []

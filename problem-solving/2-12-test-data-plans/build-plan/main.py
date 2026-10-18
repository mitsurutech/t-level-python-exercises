def kind_of_data(text, low, high):
    # A field takes a whole number from low to high, typed as text.
    # "valid"     a whole number from low to high (both included)
    # "invalid"   a whole number outside that range
    # "erroneous" text that is not a whole number, such as "abc" or "5.5" or ""
    # Use text.isdigit() to tell if the text is a whole number.
    return None


def expected_result(text, low, high):
    # "Accepted" for valid data. "Rejected" for everything else.
    return None


def data_for_test(low, high):
    # Give back a list of 6 pieces of test data, all as text, in this order:
    # low - 1, low, the middle (low + high) // 2, high, high + 1, "abc"
    # For 13 and 19 that is ["12", "13", "16", "19", "20", "abc"].
    return None


def count_failed(expected, actual):
    # expected and actual are two lists of "Accepted" and "Rejected", the same length.
    # Give back how many places are different. These are the tests that failed.
    return None

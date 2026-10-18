# An automatic test runner. A case is a pair: (input, expected answer).
# For example: (3, 6) means "when the input is 3 we expect 6".

def failed_cases(function, cases):
    # Call function with each input. Give back a list of the cases where
    # the answer was not the expected one. Keep the order.
    return []


def all_pass(function, cases):
    # True if no case failed.
    return False

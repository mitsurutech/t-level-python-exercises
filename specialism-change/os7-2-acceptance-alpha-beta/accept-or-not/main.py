# results is a list. Each item is a tuple of three things:
#   (the requirement, must_have, passed)
# For example: ("User can log in", True, True)
#   must_have is True if the client cannot accept the product without it.
#   passed is True if the test showed it works.

def accepted(results):
    # The client accepts if EVERY must-have requirement passed.
    # A nice-to-have that failed does not stop acceptance.
    return False


def not_met(results):
    # Give back a list of the requirement texts that did not pass, must-have or not,
    # in the same order as the input.
    return []

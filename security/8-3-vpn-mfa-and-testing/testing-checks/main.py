def unexpected_ports(open_ports, expected):
    # open_ports and expected are lists of port numbers.
    # Give back a sorted list of the ports that are open but NOT expected.
    return []


def is_mfa(factors):
    # factors is a list made of "know" (a password), "have" (a phone) and "are" (a fingerprint).
    # Real MFA needs at least TWO DIFFERENT kinds.
    return False


def may_test(permission_in_writing, in_scope):
    # An ethical test needs written permission AND the target must be in scope.
    return False

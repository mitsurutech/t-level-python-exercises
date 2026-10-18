def is_authorised(user, resource, permissions):
    # permissions is a dictionary: user name -> list of resources they may use.
    # Give back True only if the user may use the resource.
    return None


def access_message(user, resource, permissions):
    # Give back "Access granted" or "Access denied: ask your manager".
    return ""


def count_denied(attempts, permissions):
    # attempts is a list of pairs: [user, resource].
    # Count how many were NOT allowed.
    return None

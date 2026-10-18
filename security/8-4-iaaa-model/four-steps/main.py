import hashlib


def hash_of(text):
    # This one is done for you. It gives back the hash of the text.
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def identify(username, users):
    # users is a dictionary: username -> a record with "hash" and "role".
    # Identification: is this username known? Give back True or False.
    return False


def authenticate(username, password, users):
    # Authentication: does the hash of the password equal the stored hash? Use hash_of.
    # An unknown username is always False.
    return False


def authorise(role, action, role_permissions):
    # Authorisation (role-based): role_permissions is role -> list of actions.
    # An unknown role may do nothing.
    return False


def actions_by(log, user):
    # Accountability: log is a list of entries. Each entry is a list: [user, action].
    # Give back the list of actions done by user, in order.
    return []

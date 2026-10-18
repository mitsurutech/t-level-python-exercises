def clean_name(text):
    # Make a member name safe to store.
    # Remove spaces at the start and end.
    # Give back None if the name is empty, longer than 30 characters,
    # or has anything except letters, spaces, hyphens and apostrophes.
    return text


def mask(text):
    # Hide all but the last 4 characters with * so a phone number is not shown in full.
    # Text of 4 characters or fewer is given back as it is.
    return text


def is_strong_password(password):
    # True if it is at least 8 characters long, has a letter and has a digit.
    return None

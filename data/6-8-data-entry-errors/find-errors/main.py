def differences(typed, correct):
    # Count the places where the two texts are different.
    # They are the same length. If the lengths are not the same, give back -1.
    # Example: differences("12345", "12354") is 2.
    return 0


def is_transposition(typed, correct):
    # A transposition is when two NEXT-TO-EACH-OTHER characters swap places.
    # Give back True only if swapping one such pair in typed makes correct.
    # "1234" and "1324" is True. "1234" and "1432" is False. Two equal texts is False.
    return None


def error_type(typed, correct):
    # Give back "none" if the two are the same.
    # Give back "transposition" if is_transposition says so.
    # Otherwise give back "transcription".
    return ""


def valid_phone(text):
    # A UK mobile phone number for this form: exactly 11 characters,
    # all digits, and the first digit is 0.
    # Give back True or False.
    return None

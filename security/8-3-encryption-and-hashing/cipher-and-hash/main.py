import hashlib


def shift_letter(letter, key):
    # Move a capital letter along the alphabet by key places. Z wraps round to A.
    # shift_letter("A", 3) gives "D". Anything that is not a capital letter stays the same.
    return letter


def encrypt(message, key):
    # Use shift_letter on every letter of the message.
    return message


def decrypt(message, key):
    # The reverse. Hint: shifting back is the same as shifting forward by 26 minus key.
    return message


def hash_of(text):
    # This one is done for you. It gives back the hash of the text.
    return hashlib.sha256(text.encode("utf-8")).hexdigest()


def password_matches(typed, stored_hash):
    # True if the hash of what was typed equals the stored hash.
    return False

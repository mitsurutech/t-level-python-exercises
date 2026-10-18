import hashlib
import hmac

ROLES = {
    "student": {"read"},
    "teacher": {"read", "write"},
    "admin": {"read", "write", "delete"},
}


def has_access(role, action):
    # True only if the role exists and its set holds the action.
    # An unknown role has no access: give back False.
    return None


def hash_password(password, salt):
    # Join the salt and the password (salt first), turn the text into bytes with
    # encode(), and give back the SHA-256 hash as a hex string.
    return None


def check_password(password, salt, stored):
    # True if the password gives the stored hash.
    # Compare with hmac.compare_digest, not with ==.
    return None


def shift_encrypt(text, shift):
    # A toy cipher, NOT secure. Move each letter a to z forward by shift places.
    # z followed by one place is a. Keep the case. Leave other characters as they are.
    return None

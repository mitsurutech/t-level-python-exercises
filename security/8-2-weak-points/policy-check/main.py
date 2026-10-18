def password_problems(password):
    # Give back a list of problems. Use these exact words:
    # "too short" if under 10 characters
    # "no digit" if there is no digit 0 to 9
    # "no capital" if there is no capital letter
    # "too common" if it is in the common list
    common = ["password", "123456", "qwerty", "letmein"]
    return []


def is_out_of_date(installed, latest):
    # Versions are whole numbers. Give back True if a newer version exists.
    return False


def is_supported(year_now, support_ends):
    # The maker fixes problems until the end of the support year.
    # Give back True if the year now is the end year or earlier.
    return False

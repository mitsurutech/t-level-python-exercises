from datetime import datetime


def show_date(when):
    # when is a datetime. Give back text like 25/12/2026 (day, month, year).
    return None


def read_date(text):
    # text should look like 25/12/2026. Give back a datetime.
    # If the text is not a real date, give back None.
    return 0


def day_name(text):
    # text looks like 25/12/2026. Give back the day of the week as text, such as "Friday".
    # Use read_date().
    return None


def is_weekend(text):
    # Give back True if the date text is a Saturday or a Sunday.
    # Hint: strftime("%A") gives the day name.
    return None

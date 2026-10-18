OPEN_HOUR = 9
LAST_HOUR = 20
MEMBER_RATE = 0     # set this to the member price
VISITOR_RATE = 0    # set this to the visitor price


def rate_for(is_member):
    # Give back the rate for one hour. Use the two constants above.
    return None


def to_hour(text):
    # text is what a person typed. Use try and except.
    # Give back the hour as an integer if it is a whole number from OPEN_HOUR to LAST_HOUR.
    # Give back None for anything else, such as "abc", "" or "10.5".
    return None


def average_hour(texts):
    # texts is a list of typed hours. Use to_hour for each one.
    # Skip the bad ones. Give back the average of the good ones, rounded to 1 decimal place.
    # Give back None if there are no good ones.
    return None

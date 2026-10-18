def normalise_choice(text):
    # Make a typed answer easy to compare: no spaces at the start or end, all lower case.
    # " Yes " becomes "yes".
    return None


def format_price(pounds):
    # Give the price with 2 decimal places and the word pounds.
    # 8 becomes "8.00 pounds". 4.5 becomes "4.50 pounds".
    return None


def menu_text(options):
    # options is a list of words. Give back one line for each, numbered from 1,
    # joined with a new line: "1. Book a court" then "2. Cancel a booking".
    return None


def booking_message(result, court, hour):
    # result is "ok", "closed", "taken" or "bad_court". Give back a message a person understands.
    # ok: say the court and the hour were booked.
    # closed: say the club is closed at that hour, and say it is open from 9 to 20.
    # taken: say that court is already booked at that hour, and say to try another.
    # bad_court: say there is no such court, and say the courts are 1 and 2.
    # Anything else: say that something went wrong.
    return None

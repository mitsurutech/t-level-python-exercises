OPEN_HOUR = 9
LAST_HOUR = 20


def is_free(bookings, court, hour):
    # This one is finished. Use it.
    for one in bookings:
        if one["court"] == court and one["hour"] == hour:
            return False
    return True


def book(bookings, member, court, hour):
    # Add a booking and give back True.
    # Give back False and add nothing if:
    #   the hour is before OPEN_HOUR or after LAST_HOUR,
    #   the court is not 1 or 2,
    #   or the court is not free at that hour.
    # A booking is a dictionary: {"member": ..., "court": ..., "hour": ...}
    return None


def cancel(bookings, member, court, hour):
    # Remove that member's booking and give back True.
    # Give back False if there is no such booking for that member.
    return None

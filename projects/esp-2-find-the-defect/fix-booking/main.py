def price_for(is_member, hours):
    # Members pay 4 pounds an hour. Visitors pay 6 pounds an hour.
    rate = 6 if is_member else 4
    return rate * hour


def is_free(bookings, court, hour):
    # A court is free if nobody has the same court at the same hour.
    for one in bookings:
        if one["court"] == court or one["hour"] == hour:
            return False
    return True


def count_for(bookings, member):
    # How many bookings does this member have?
    total = 0
    for one in bookings:
        if one["member"] == member:
            total = 1
    return total

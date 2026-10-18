def is_free(bookings, court, hour):
    for one in bookings:
        if one["court"] == court and one["hour"] == hour:
            return False
    return True


def book(bookings, member, court, hour):
    if hour < 9 or hour > 20 or court not in (1, 2):
        return False
    if not is_free(bookings, court, hour):
        return False
    bookings.append({"member": member, "court": court, "hour": hour})
    return True


def cancel(bookings, member, court, hour):
    for one in bookings:
        if one["member"] == member and one["court"] == court and one["hour"] == hour:
            bookings.remove(one)
            return True
    return False


def next_in_line(waiting, court, hour):
    for one in waiting:
        if one["court"] == court and one["hour"] == hour:
            return one["member"]
    return None


def leave_waiting_list(waiting, member, court, hour):
    for one in waiting:
        if one["member"] == member and one["court"] == court and one["hour"] == hour:
            waiting.remove(one)
            return True
    return False


def cancel_and_promote(bookings, waiting, member, court, hour):
    # Cancel the member's booking. If somebody is waiting for that court and hour,
    # give the court to the first person and take them off the waiting list.
    # Give back the name of the person who got the court, or None.
    # The parts above each pass their own tests. The problem is where they join.
    cancel(bookings, member, court, hour)
    promoted = next_in_line(waiting, court, hour)
    if promoted is not None:
        book(bookings, promoted, court, hour)
    return promoted

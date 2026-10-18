def join_waiting_list(waiting, member, court, hour):
    # Finished for you. waiting is a list of dictionaries.
    place = 0
    for one in waiting:
        if one["court"] == court and one["hour"] == hour:
            if one["member"] == member:
                return 0
            place = place + 1
    waiting.append({"member": member, "court": court, "hour": hour})
    return place + 1


def next_in_line(waiting, court, hour):
    # Give back the name of the first member waiting for this court and hour.
    # Give back None if nobody is waiting for it.
    return 0


def leave_waiting_list(waiting, member, court, hour):
    # Remove this member's entry for this court and hour.
    # Give back True if it was removed, False if it was not there.
    return None

def join_waiting_list(waiting, member, court, hour):
    # An AI tool wrote this. Check it, then fix it.
    # waiting is a list of dictionaries: {"member": ..., "court": ..., "hour": ...}
    # Add the member to the list and give back their place in the line for that court and hour.
    # Place 1 means first. Give back 0 and add nothing if the member is already waiting for the same court and hour.
    for one in waiting:
        if one["member"] == member:
            return 0
    waiting.append({"member": member, "court": court, "hour": hour})
    return len(waiting)

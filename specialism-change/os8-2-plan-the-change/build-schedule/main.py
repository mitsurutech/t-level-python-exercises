# Each change request is a dictionary:
#   {"name": "Fix login bug", "priority": 1, "days": 2}
# priority 1 is the most urgent. 3 is the least urgent.
# days is how long the change takes.

def put_in_order(requests):
    # Finished for you. Gives back a new list in schedule order:
    # priority 1 first. For the same priority, fewer days first.
    def order(one):
        return [one["priority"], one["days"]]
    return sorted(requests, key=order)


def schedule(requests):
    # Give back the NAMES in the order we should do them.
    # Hint: loop over put_in_order(requests) and add one["name"] to a list.
    return []


def fits(requests, days_available):
    # Go through put_in_order(requests). Add each name
    # while it still fits in the days left. Stop at the first one that does not fit.
    # Give back the list of names that fit.
    return []

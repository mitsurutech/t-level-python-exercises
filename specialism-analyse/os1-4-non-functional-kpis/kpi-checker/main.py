def response_ok(response_ms, limit_ms):
    # Responsiveness: the page must answer in limit_ms milliseconds or less.
    # Give back True or False.
    return None


def load_ok(users_now, users_allowed):
    # Load handling: the system must cope with users_allowed users at once.
    # Give back True if users_now is not more than users_allowed.
    return None


def reliable(downtime_minutes, allowed_minutes):
    # Reliability: the system may be down for allowed_minutes in a month, no more.
    # Give back True if downtime_minutes is within that limit.
    return None


def report(response_ms, users_now, downtime_minutes):
    # Targets: 2000 milliseconds, 500 users, 45 minutes.
    # Give back a list of the names of the KPIs that FAIL, in this order:
    # "responsiveness", "load", "reliability". An empty list means all pass.
    return None

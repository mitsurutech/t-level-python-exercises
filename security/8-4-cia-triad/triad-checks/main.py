def which_goal(event):
    # Give back "confidentiality", "integrity" or "availability" for each event.
    # "stolen password list" -> confidentiality
    # "marks changed by a stranger" -> integrity
    # "website down for two hours" -> availability
    # Give back "unknown" for anything else.
    return ""


def is_unchanged(text, saved_copy):
    # True if text is exactly the same as the saved copy.
    return False


def available_minutes(total_minutes, outages):
    # outages is a list of whole numbers: minutes of each outage.
    # Give back the minutes the system WAS available.
    return 0

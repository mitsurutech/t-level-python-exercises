def total_hours(build_hours, forms, minutes_each):
    # Hours to build the screen, plus the hours to type in all the forms.
    # There are 60 minutes in an hour.
    # Example: total_hours(2, 120, 3) is 8.0 (2 hours + 360 minutes, which is 6 hours).
    return 0


def best_option(options, forms):
    # options is a list of dictionaries, like:
    # {"name": "Plain boxes", "build_hours": 2, "minutes_each": 3}
    # Give back the name of the option with the smallest total hours for that many forms.
    # If two are equal, give back the one that comes first in the list.
    return ""


def worth_building(forms, minutes_saved_each, build_hours):
    # A new screen saves minutes_saved_each minutes on every form.
    # Give back True if the hours saved are MORE than the hours to build it.
    return None

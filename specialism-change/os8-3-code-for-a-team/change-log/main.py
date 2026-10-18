# A change log is a short list of what changed in each version, newest first.
# One entry is a dictionary: {"version": "2.1.0", "day": "2026-10-17", "kind": "Fixed", "text": "Login accepts spaces"}
# kind is one of: Added, Changed, Fixed.

def log_line(entry):
    # Give back one line of text like:
    # 2.1.0 (2026-10-17) [Fixed] Login accepts spaces
    return ""


def newest_first(entries):
    # Finished for you. Gives back a new list, newest day first.
    # The days look like 2026-10-17, so text order is date order.
    def day_of(entry):
        return entry["day"]
    return sorted(entries, key=day_of, reverse=True)


def change_log(entries):
    # Give back one text with a log_line for each entry, newest day first.
    # Put a new line ("\n") between two lines, and none at the end.
    # Hint: loop over newest_first(entries). Start with text = "".
    # Before each line, add "\n" if text is not empty yet.
    return ""

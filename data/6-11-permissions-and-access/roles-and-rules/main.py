PERMISSIONS = {
    "student": ["read_own_marks"],
    "teacher": ["read_own_marks", "read_class_marks", "edit_marks"],
    "admin": ["read_own_marks", "read_class_marks", "edit_marks", "delete_student"],
}


def can_do(role, action):
    # Role-based: look up the role in PERMISSIONS.
    # Give back True if the role may do the action, else False.
    # An unknown role may do nothing.
    return None


def office_open(hour):
    # Rule-based: the system works from 9 in the morning until 5 in the evening.
    # hour is a whole number from 0 to 23. So 9 is open and 16 is open, but 17 is closed.
    # Give back True or False.
    return None


def can_access(role, action, hour):
    # Both must be true: the role may do the action AND the office is open.
    return None

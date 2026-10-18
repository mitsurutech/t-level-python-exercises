def scan(files, signatures):
    # files is a dictionary: file name -> the text inside it.
    # signatures is a list of known bad text snippets.
    # Give back a sorted list of the names of files that contain ANY signature.
    return []


def failed_login_alerts(attempts, limit):
    # attempts is a list of entries. Each entry is a list: [user, worked].
    # For example [["sam", True], ["eve", False], ["eve", False]].
    # worked is True if the login worked and False if it failed.
    # Give back a sorted list of users with limit or more FAILED logins.
    return []


def can_do(role, action, policy):
    # policy is a dictionary: role -> list of actions that role may do.
    # Give back True only if the role has the action. An unknown role may do nothing.
    return False

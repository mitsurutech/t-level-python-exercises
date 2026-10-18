def check_age(text):
    # text is what the user typed. Give back one of these:
    #   "Age is required"            if text is empty
    #   "Please enter a number"      if text is not made of digits
    #   "Age must be 0 to 120"       if the number is outside 0 to 120
    #   "ok"                         otherwise
    return None


def check_username(name):
    # True if the name is 3 to 12 characters and only letters or digits. Else False.
    return None


def price_of(menu, item):
    # menu is a dictionary of item to price. Give back the price, or None if the item is not on the menu.
    return None


def undo(history):
    # history is a list of actions. It is a stack: the last action added is the first one removed.
    # Remove the last action from the list and give it back. If the list is empty, give back None.
    return "nothing"


def serve_next(queue):
    # queue is a list. It is a queue: the first person added is the first one served.
    # Remove the first person and give them back. If the list is empty, give back None.
    return "nobody"

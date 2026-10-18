def kind_of_info(item):
    # Give back "hr", "commercial" or "access" for each kind of secret.
    # Give back "unknown" if the item is not on the lists.
    # Right now this gives back "", which is wrong.
    hr = ["salary", "staff address", "bonus", "sick pay"]
    commercial = ["client list", "sales numbers", "contract", "product design"]
    access = ["password", "pin", "fingerprint", "access code"]
    return ""


def must_protect(item):
    # Give back True if the item is on any of the three lists.
    return False

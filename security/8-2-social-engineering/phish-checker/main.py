def domain_of(url):
    # Give back the site name part of a web address.
    # "https://bank.co.uk/login" gives "bank.co.uk"
    return ""


def is_real_site(url, real_domain):
    # True only if the site name is EXACTLY the real one.
    return False


def red_flags(message):
    # Count how many of these warning words are in the message (any capital letters).
    words = ["urgent", "password", "verify", "winner", "gift", "immediately"]
    return 0

def combinations(symbols, length):
    # symbols is how many different characters can be used. length is how many are typed.
    # A 4 digit PIN has 10 symbols and a length of 4, so 10000 combinations.
    return 0


def escape_html(text):
    # Swap the dangerous characters so a browser shows them as text and does not run them.
    # & becomes &amp;   < becomes &lt;   > becomes &gt;
    return text


def username_ok(name):
    # A good username is 3 to 12 characters long, and only letters and digits.
    return True

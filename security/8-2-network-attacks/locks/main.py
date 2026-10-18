def api_reply(key, valid_keys, wanted):
    # An API holds some data. It must only answer a caller with a valid key.
    # Give back the data in wanted if key is in valid_keys.
    # If not, give back the word "denied".
    return ""


def wifi_advice(has_password, uses_https):
    # Give back one word of advice for a person on a Wi-Fi network:
    #   "safe"    if the network has a password AND the site uses https
    #   "careful" if only one of the two is true
    #   "avoid"   if neither is true
    return ""

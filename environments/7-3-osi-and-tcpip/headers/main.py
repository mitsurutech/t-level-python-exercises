def add_headers(message):
    # Add three labels in front of the message, one at a time:
    # first "[TCP]", then "[IP]", then "[Frame]".
    # Each new label goes at the very front.
    # add_headers("Hi") gives "[Frame][IP][TCP]Hi".
    return message


def remove_headers(packet):
    # The other computer takes the labels off in the opposite order.
    # remove_headers("[Frame][IP][TCP]Hi") gives "Hi".
    return packet

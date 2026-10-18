# A college form asks for an age. Only 16, 17, 18 and 19 are allowed.
# The user types text, so the value is always a string, for example "17" or "abc".
#
# Give back one of three answers:
#   "ok"             the text is a whole number from 16 to 19
#   "wrong range"    the text is a whole number, but it is below 16 or above 19
#   "not a number"   the text is not made only of digits: letters, empty, 16.5 or -3
#                    (the dot and the minus sign are not digits)
#
# Hint: "17".isdigit() is True. "abc".isdigit() is False.

def check_age(text):
    return ""

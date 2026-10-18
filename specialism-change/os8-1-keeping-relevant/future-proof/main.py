# A food delivery app charges a delivery fee. Today the fee is 3.00 and
# delivery is free when the basket is 20.00 or more.
# These numbers are written inside the code in many places. Next year they will change.
# Put them in ONE settings dictionary, and make the functions read it.

def default_settings():
    # Give back a dictionary with two keys: "fee" (3.0) and "free_over" (20.0).
    return {}


def delivery_fee(basket_total, settings):
    # 0 if basket_total is free_over or more, otherwise the fee.
    return 0


def order_total(basket_total, settings):
    # The basket plus the delivery fee.
    return 0

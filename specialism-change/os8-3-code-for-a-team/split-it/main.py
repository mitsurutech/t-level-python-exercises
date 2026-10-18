# This function works, but it does everything in one place.
# Split it into small functions. Each one does ONE job.

def line_total(price, qty):
    # price times qty
    return 0


def basket_total(items):
    # items is a list of (name, price, qty). Give back the total of all the lines.
    return 0


def receipt_line(name, price, qty):
    # Give back text like: Tea x2 = 3.00   (x2 means 2 teas. The total has 2 decimal places)
    return ""


def receipt(items):
    # This one is the old long version. Rewrite it so it USES the three functions above.
    text = ""
    total = 0
    for name, price, qty in items:
        cost = price * qty
        text = text + name + " x" + str(qty) + " = " + format(cost, ".2f") + "\n"
        total = total + cost
    text = text + "Total = " + format(total, ".2f")
    return text

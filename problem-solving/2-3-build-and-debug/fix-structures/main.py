def last_item(items):
    # Give back the last item in the list.
    return items[len(items)]


def sorted_scores(scores):
    # Give back the scores in order, lowest first.
    return scores.sort()


def safe_price(menu, item):
    # Give back the price. If the item is not on the menu, give back 0.
    return menu[item]


def first_item(items):
    # Give back the first item in the list.
    return items[1]

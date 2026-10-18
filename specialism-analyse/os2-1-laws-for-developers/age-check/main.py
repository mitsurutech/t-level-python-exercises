def pegi_allowed(age, pegi_rating):
    # A game has a PEGI age rating: 3, 7, 12, 16 or 18.
    # A player may play it if their age is the same as the rating or higher.
    # Give back True or False.
    return None


def can_consent_alone(age):
    # In the UK, a child can agree to the use of their personal data by an online
    # service on their own from age 13. Give back True if age is 13 or more.
    return None


def check_game(age, pegi_rating, collects_data):
    # Give back one of these words:
    # "blocked"   if the player is too young for the rating
    # "ask parent" if the game collects data and the player cannot consent alone
    # "ok"        otherwise
    return None

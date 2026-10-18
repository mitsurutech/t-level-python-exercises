def risk_score(likelihood, seriousness):
    # Both are whole numbers from 1 (very low) to 5 (very high).
    # The score is likelihood multiplied by seriousness.
    return 0


def risk_level(score):
    # 1 to 5 is "low", 6 to 14 is "medium", 15 or more is "high".
    return None


def worst_risk(risks):
    # risks is a list of dictionaries like:
    # {"name": "Server fails", "likelihood": 2, "seriousness": 5}
    # Give back the name of the risk with the highest score.
    # If two are equal, give back the one that comes first in the list.
    return None

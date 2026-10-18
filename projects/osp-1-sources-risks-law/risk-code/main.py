def risk_score(likelihood, impact):
    # likelihood and impact are whole numbers from 1 (low) to 3 (high).
    # The score is likelihood times impact.
    return None


def risk_level(score):
    # 1 or 2 is "low". 3 or 4 is "medium". 5 or more is "high".
    return None


def worst_risk(risks):
    # risks is a list like [("Data loss", 2, 3), ("Late finish", 3, 2)]
    # Each is (name, likelihood, impact).
    # Give back the name of the risk with the highest score.
    # If two are equal, give back the one that comes first in the list.
    # Give back None for an empty list.
    return 0

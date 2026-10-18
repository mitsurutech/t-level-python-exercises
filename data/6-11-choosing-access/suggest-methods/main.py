def suggest_methods(many_platforms, needs_rule):
    # Give back a list of access methods for a system. Use this order:
    #   "RBAC"       always (every system gives permissions by role)
    #   "RuBAC"      if needs_rule is True (a time or place rule is needed)
    #   "API"        if many_platforms is True (a phone app, a website, partners)
    return []


def risk_level(sensitive, many_platforms):
    # "high" if the data is sensitive AND many platforms use it.
    # "medium" if only one of those is True.
    # "low" if neither.
    return ""

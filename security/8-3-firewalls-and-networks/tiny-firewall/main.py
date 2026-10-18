def decide(rules, direction, port):
    # rules is a list of rules, in order. Each rule is a list: [action, direction, port].
    # For example ["allow", "in", 443].
    # A port of "any" matches every port. The FIRST rule that matches wins.
    # If no rule matches, the answer is "deny" (default deny).
    return ""


def ip_allowed(ip, blocked_ips):
    # False if the address is on the blocked list.
    return True


def can_talk(zone_a, zone_b, allowed_pairs):
    # allowed_pairs is a list of pairs, like [["office", "servers"]].
    # The two zones in a pair may talk, in either direction.
    # Give back True only if the two zones are the same, or the pair is allowed.
    return True

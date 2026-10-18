def servers_needed(users):
    # Each server handles 100 users. Always keep at least 1 server running.
    # 250 users need 3 servers, because 2 servers handle only 200.
    return 0


def cloud_cost_pence(servers, hours, pence_per_hour):
    # Pay as you go: every server costs pence_per_hour for every hour it runs.
    # Give back the total cost in pence.
    return 0

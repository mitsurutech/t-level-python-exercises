def where_runs(needs_other_players, must_be_trusted):
    # A job runs "remote" (on the server) if it needs data from other players
    # or if the result must be trusted (so nobody can cheat).
    # Otherwise it runs "local" (on the player's own device).
    return None


def make_plan(jobs):
    # jobs is a dictionary: name -> (needs_other_players, must_be_trusted)
    # Give back a dictionary: name -> "local" or "remote".
    return None


def count_remote_calls(plan):
    # How many jobs in the plan run "remote"?
    return None

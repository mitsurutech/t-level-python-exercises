def format_event(time, level, message):
    # One log line per event, as text: time, level and message, joined by one space.
    # Example: format_event("2026-10-17T09:00:00", "INFO", "started") gives
    #   2026-10-17T09:00:00 INFO started
    return None


def workers_needed(users, users_per_worker):
    # Scale out: how many workers (copies of the process) are needed?
    # Every user must be served, so round up.  250 users, 100 per worker: 3 workers.
    # At least 1 worker, even with 0 users.
    # Hint: start with 1 worker and add one more until workers * users_per_worker is at least users.
    return None


def stop_gracefully(jobs, finish):
    # Graceful shutdown: call finish(job) for every job in the list, in order.
    # Give back how many jobs were finished.
    return None

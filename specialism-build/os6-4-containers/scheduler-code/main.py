def containers_to_change(desired, running):
    # desired is how many copies we want. running is how many are running now.
    # Give back a dictionary with two keys, "start" and "stop".
    # Example: desired 3, running 1 gives {"start": 2, "stop": 0}.
    return None


def failed_containers(states):
    # states is a dictionary like {"web-1": "running", "web-2": "failed"}.
    # Give back the names of the failed ones, in alphabetical order, as a list.
    return None


def copies_needed(requests_per_second, per_container):
    # Each container handles per_container requests a second.
    # Give back how many containers we need. Always round UP, and never go below 1.
    # Example: 250 requests with 100 each needs 3.
    return None


def container_name(image, number):
    # Give back text like: web-2
    return None

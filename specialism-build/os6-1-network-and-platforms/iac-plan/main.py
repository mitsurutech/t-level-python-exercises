def plan(desired, current):
    # desired and current are dictionaries: server name -> size, like {"web": "small"}.
    # Give back a list of actions, as pairs, in this order:
    #   first every ("create", name)  for a name only in desired,
    #   then  every ("update", name)  for a name in both with a different size,
    #   then  every ("delete", name)  for a name only in current.
    # Inside each group, sort the names A to Z.
    return None


def summary(actions):
    # Give back text like: 1 to create, 2 to update, 0 to delete
    return None

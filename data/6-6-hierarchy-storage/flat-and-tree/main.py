def to_tree(rows):
    # rows is a flat list. Each row is a list of two items: [department, name].
    # Give back a dictionary: each department points to a list of its names, in order.
    # [["Maths", "Ava"], ["Art", "Ben"], ["Maths", "Cy"]]
    # gives {"Maths": ["Ava", "Cy"], "Art": ["Ben"]}
    return None


def to_flat(tree):
    # The opposite. Give back a flat list of [department, name] rows.
    # Go through the departments in order, and through each list of names in order.
    return None


def count_names(tree, department):
    # Give back how many names are in that department. Give back 0 if there is no such department.
    return None


def chain_to_top(parents, name):
    # parents says who each person reports to. The top person has None.
    # {"Head": None, "Ava": "Head", "Ben": "Ava"}
    # chain_to_top(parents, "Ben") gives ["Ben", "Ava", "Head"]
    return None

def make_table(conn):
    # Make a table called players with three columns:
    # id (whole number, primary key), name (text) and points (whole number).
    pass


def add_player(conn, name, points):
    # Add one row. Use ? placeholders, never join the text yourself.
    pass


def get_points(conn, name):
    # Give back the points of the player with this name, or None if there is no such player.
    return None


def update_points(conn, name, points):
    # Change the points of that player.
    pass


def delete_player(conn, name):
    # Remove that player.
    pass

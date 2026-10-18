import sqlite3


def make_db():
    # Give back a new in-memory database with a table:
    # scores(name TEXT PRIMARY KEY, points INTEGER)
    return None


def add_score(db, name, points):
    # Insert a row. Use ? placeholders, never join the text yourself.
    pass


def update_score(db, name, points):
    # Change the points of an existing player.
    pass


def delete_score(db, name):
    # Remove the player's row.
    pass


def all_scores(db):
    # Give back a list of (name, points) tuples, sorted by name.
    return None

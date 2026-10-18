import json


def build_url(base, endpoint, params):
    # Join the base address, a slash and the endpoint. If params is not empty,
    # add a question mark and the parameters as name=value pairs joined by &.
    # build_url("http://api.test", "scores", {"player": "Aisha"})
    #   gives "http://api.test/scores?player=Aisha"
    return None


def top_player(json_text):
    # json_text is a JSON list of players, such as
    # '[{"player": "Aisha", "points": 12}, {"player": "Sam", "points": 30}]'
    # Give back the name of the player with the most points.
    return None


def score_lines(json_text):
    # Give back a list of text lines like "Aisha: 12 points", in the same order.
    return None


def with_key(url, key):
    # Add the API key to the address. If the address already has a question mark,
    # add &key=... , otherwise add ?key=...
    return None

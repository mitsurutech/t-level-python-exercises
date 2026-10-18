import json
import random
from collections import Counter
from datetime import date


def count_words(text):
    # Count each word, ignoring upper and lower case. Words are split by spaces.
    # Give back a dictionary, like {"the": 2, "cat": 1}. Use collections.Counter.
    return None


def order_total(json_text):
    # json_text is like: {"items": [{"name": "tea", "price": 150}, {"name": "milk", "price": 90}]}
    # Give back the sum of the prices (pence). Use json.loads.
    return None


def days_until(today_text, due_text):
    # Both are dates written like 2026-11-05. Give back the number of days from
    # today to the due date. Use datetime.date.fromisoformat.
    return None


def pick_winner(names, seed):
    # Pick one name. With the same seed the same name must come back every time.
    # Use random.Random(seed).
    return None

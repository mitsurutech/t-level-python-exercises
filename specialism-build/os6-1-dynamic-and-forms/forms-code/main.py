from html import escape
from urllib.parse import parse_qs
from http.cookies import SimpleCookie


def build_page(title, items):
    # Give back text like: <h1>Shop</h1><ul><li>Tea</li><li>Milk</li></ul>
    # Use escape() on the title and on every item, so a user cannot add a tag.
    return None


def handle_form(body):
    # body is form data as text, like: name=Sam&age=15
    # Good data: give back {"ok": True, "name": "Sam", "age": 15}  (age is a whole number)
    # Name missing or only spaces: {"ok": False, "error": "Name is missing."}
    # Age not a whole number:      {"ok": False, "error": "Age must be a whole number."}
    # Age under 1 or over 120:     {"ok": False, "error": "Age must be between 1 and 120."}
    # Check the name first, then the age.
    return None


def parse_cookie(header):
    # header is like: theme=dark; user=sam
    # Give back a dictionary: {"theme": "dark", "user": "sam"}
    return None


def make_cookie(name, value):
    # Give back text like: user=sam; HttpOnly; Path=/
    return None

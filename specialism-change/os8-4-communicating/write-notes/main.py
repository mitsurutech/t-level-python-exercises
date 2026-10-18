# Release notes tell USERS what changed, in plain words.
# changes is a list of dictionaries: {"kind": "Added", "text": "Dark mode"}
# kind is "Added", "Fixed" or "Changed".
#
# Give back text like this (a new line between the lines):
#   Version 2.1.0
#   New:
#   - Dark mode
#   Fixed:
#   - Login accepts spaces
# "Added" is shown as "New:". "Fixed" is "Fixed:". "Changed" is "Changed:".
# The groups come in the order New, Fixed, Changed. A group with no items is left out.

def release_notes(version, changes):
    return ""

# A tiny static analyser. It reads code as text. It never runs it.
# Each line of the code is one string in the list "lines".

def find_problems(lines):
    # Give back a list of the line numbers (the first line is 1) that have a problem.
    # A line has a problem if it contains any of these:
    #   a password written in the code: the text  password =
    #   the dangerous function: the text  eval(
    #   an address that is not secure: the text  http://
    return []

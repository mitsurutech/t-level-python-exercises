# Ticket 231: a teacher opens the marks page for a new class with no marks yet.
# The page shows an error. The bug is in these two functions. Fix them.
#   average_mark(marks): the average of the list. For an empty list give back 0.
#   top_mark(marks): the biggest mark. For an empty list give back None.
# Do not break the normal case.

def average_mark(marks):
    return sum(marks) / len(marks)


def top_mark(marks):
    return max(marks)

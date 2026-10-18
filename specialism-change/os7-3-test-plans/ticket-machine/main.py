# A bus ticket machine. The plan says:
#   Under 5: free (0).  Age 5 to 15: child fare 1.0.  Age 16 and over: adult fare 2.5.
#   A student aged 16 or over pays 1.5.  A child who is a student still pays 1.0.
#   An age below 0 is a mistake: use raise ValueError(...) to stop with an error.
# The code below has FOUR bugs. The tests in the plan found them. Fix them.

def ticket_price(age, is_student=False):
    if age <= 5:
        return 0
    if age < 15:
        return 1.0
    if is_student:
        return 2.5
    return 2.5

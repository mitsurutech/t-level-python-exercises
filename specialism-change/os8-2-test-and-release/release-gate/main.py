# results is a list of tests. Each one is a tuple: (name, critical, passed).
#   critical is True if the product cannot go out with this test failing.
#   passed is True if the test passed after the change.
# kind is "planned" or "reactive".

def can_release(results, kind):
    # planned release: every test must pass.
    # reactive release (an urgent fix): every CRITICAL test must pass.
    #   other failed tests are allowed, but they must be fixed later.
    return False


def must_fix_later(results):
    # The names of the tests that failed and are not critical. Keep the order.
    return []

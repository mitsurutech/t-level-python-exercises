# An API contract is a file that describes an API so that PROGRAMS can read it.
# Here it is a Python dictionary. The keys under "paths" are addresses.
# Under each address are the methods allowed, for example "get" or "post".
#
# contract = {"paths": {"/users": {"get": {}, "post": {}}, "/users/1": {"get": {}}}}
#
# Give back a list of text like "GET /users", one for each address and method.
# Write the method in capital letters. Sort the list in alphabetical order.

def list_endpoints(contract):
    return []

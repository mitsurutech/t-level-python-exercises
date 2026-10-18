def parse_connection_string(text):
    # Turn "DSN=ShopDSN;UID=student;PWD=pw" into {"DSN": "ShopDSN", "UID": "student", "PWD": "pw"}.
    # Split on ";". Ignore empty parts. Split each part at the FIRST "=" only.
    # Make every name upper case, so "dsn=x" gives the name "DSN".
    return None


def find_source(sources, name):
    # sources is a dictionary: data source name -> details.
    # Give back the details for this name, or None if there is no such data source.
    return None


def open_connection(sources, drivers, text):
    # Work like a driver manager.
    # 1. Read the connection string. 2. Find the data source named by DSN.
    # 3. Find the driver: it is drivers[details["driver"]], a function.
    # 4. Give back driver(details, user), where user is the UID (use "" if there is none).
    # No such data source: give back "Data source not found".
    # No such driver: give back "Driver not found".
    return None

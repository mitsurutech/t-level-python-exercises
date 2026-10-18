POOL = ["192.168.1.10", "192.168.1.11", "192.168.1.12"]
NAMES = {"files.lab": "10.0.10.5", "printer.lab": "10.0.10.6"}


def dns_lookup(name):
    # Give back the address for the name, or "not found".
    return ""


def dhcp_lease(leased):
    # leased is the list of addresses already given out.
    # Give back the first address in POOL that is not in leased.
    # If none is left, give back "no address left".
    return ""

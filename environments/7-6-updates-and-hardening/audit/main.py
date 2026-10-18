def unneeded_ports(open_ports, needed_ports):
    # open_ports is a list of port numbers that are open now.
    # needed_ports is a list of ports the system really uses.
    # Give back the open ports that are not needed, in order from the smallest.
    return []


def needs_patch(installed_version, fixed_version):
    # The maker has fixed a weakness in fixed_version.
    # Give back True if the installed version is older than the fixed one.
    return False

def hosts_needed(vms, vms_per_host):
    # How many hosts do we need? Each host holds vms_per_host virtual machines.
    # 21 virtual machines at 5 for each host need 5 hosts, because 4 hosts hold only 20.
    return 0


def yearly_saving(old_count, old_cost, new_count, new_cost):
    # The old way: old_count machines, each costing old_cost a year.
    # The new way: new_count hosts, each costing new_cost a year.
    # Give back how much money is saved in a year.
    return 0

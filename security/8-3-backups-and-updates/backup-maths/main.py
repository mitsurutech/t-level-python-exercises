def night_size(kind, full_size, changed_per_day, night):
    # A full backup was taken on night 0. This is the size of the backup taken on night 1, 2, 3 ...
    # "full": a whole new copy every night.
    # "incremental": only what changed since the night before.
    # "differential": everything that changed since the full backup on night 0.
    return 0


def pieces_to_restore(kind, night):
    # How many backups must be put back to restore the system after night number night (1 or more)?
    # "full": 1. "incremental": the full backup plus every night. "differential": the full backup plus the last night.
    return 0

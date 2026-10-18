def read_settings(env):
    # env is a dictionary of settings, like {"PORT": "9000", "DATABASE_URL": "db://x"}.
    # Give back a dictionary with three keys:
    #   "port"         the PORT setting as a whole number. If there is none, use 8000.
    #   "debug"        True if DEBUG is the text "true" (any case), else False. No DEBUG means False.
    #   "database_url" the DATABASE_URL setting.
    # If DATABASE_URL is missing, raise a ValueError. Never guess a password.
    return None


def missing_dependencies(declared, used):
    # declared: the list of package names written in the requirements file.
    # used: the list of package names the code imports.
    # Give back the names that are used but not declared, A to Z, with no repeats.
    return None

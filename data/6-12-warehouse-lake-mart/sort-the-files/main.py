def where_does_it_go(filename):
    # A shop chain keeps files in three places.
    #   "data lake"       raw files, as they arrive (for example till_7.log)
    #   "data warehouse"  cleaned files, whose names start with "clean_"
    #   "data mart"       a slice for one team, whose names start with "mart_"
    # Give back the name of the place for this file name.
    # Hint: filename.find("clean_") gives 0 when the name starts with clean_
    return ""


def sort_files(names):
    # Give back a dictionary with the three places as keys.
    # Each value is the list of file names that belong there, in the order given.
    return {}


def count_raw(names):
    # How many of the files are raw (they belong in the data lake)?
    return -1

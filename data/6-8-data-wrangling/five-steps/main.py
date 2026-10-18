def structure(line):
    # Step 1. Split the line on commas. Take the spaces off each part.
    # "  sam patel ,16, ls1 1ab , £4.50 " becomes ["sam patel", "16", "ls1 1ab", "£4.50"]
    return []


def clean(fields):
    # Step 2. Tidy the four fields and give back a dictionary:
    # name: all capital letters ("sam patel" becomes "SAM PATEL")
    # age: a whole number
    # postcode: all capital letters
    # price: a number with a decimal point, with the £ sign taken off
    return {}


def validate(record):
    # Step 3. Give back True only if ALL are true:
    # age is from 11 to 19, the postcode has a space in it, the price is 0 or more.
    return None


def enrich(record):
    # Step 4. Give back a copy of the record with one new key, "ticket":
    # "junior" if the age is under 16, otherwise "standard".
    return {}


def output(records):
    # Step 5. Give back text. The first line is: name,age,postcode,ticket
    # Then one line for each record, with the values in that order, joined by commas.
    # Join the lines with a new line mark. Do not put a new line mark at the end.
    return ""


def wrangle(lines):
    # This function is finished. It uses your five steps.
    good = []
    for line in lines:
        record = clean(structure(line))
        if validate(record):
            good.append(enrich(record))
    return output(good)

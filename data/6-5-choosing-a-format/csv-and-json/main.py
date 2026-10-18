def csv_to_people(text):
    # text is CSV with the headings name,age,paid. Lines are split by a newline.
    # Give back a list with one dictionary for each person after the heading line.
    # Example dictionary: {"name": "Sam", "age": 16, "paid": 12.5}
    # age must be an integer and paid must be a float, not text.
    # Hint: text.split("\n"), line.split(","), int(...), float(...)
    return None


def people_to_csv(people):
    # people is a list of dictionaries like the one above.
    # Give back CSV text. The first line is: name,age,paid
    # Put a newline between lines. Do not put one at the end.
    return None

def average(marks):
    # Found in review: the average is wrong, and an empty list must give 0.
    return sum(marks) / (len(marks) + 1)


def count_passes(marks, pass_mark):
    # Found in review: a mark equal to the pass mark is a pass.
    count = 0
    for mark in marks:
        if mark > pass_mark:
            count = count + 1
    return count


def best_student(names, marks):
    # Found in review: this gives the WORST student.
    return names[marks.index(min(marks))]


def is_valid_mark(mark):
    # Found in review: 0 and 100 are both valid marks.
    return 0 < mark < 100

# Build plan: Python exercise for T Level Digital Software Development

> **From the lesson:** [2.12: Test data and test plans](https://mitsurutech.co.uk/resources/t-level/dsd-2-12-test-data-plans)

## What to do

Build the parts of a test plan for a field that takes a whole number from `low` to `high`, typed as text.

1. `kind_of_data(text, low, high)` gives back "valid", "invalid" or "erroneous". Text that is not a whole number is erroneous. Use `text.isdigit()`.
2. `expected_result(text, low, high)` gives back "Accepted" for valid data and "Rejected" for the rest.
3. `data_for_test(low, high)` gives back six pieces of test data as text. They are: below the low edge, the low edge, the middle, the high edge, above the high edge, and "abc". For the middle use `(low + high) // 2`. This adds them, divides by 2 and drops any decimal part.
4. `count_failed(expected, actual)` counts the places where two lists of results are different.

## Starter files

- `main.py`

Write your answer in `main.py`. To try it, add a few `print(...)` lines at the bottom and run `python3 main.py`.

## Stuck?

Read the free [lesson preview](https://mitsurutech.co.uk/resources/t-level/dsd-2-12-test-data-plans), which explains the idea and lets you try its first activities. All the lessons have [free previews](https://mitsurutech.co.uk/resources/t-level).

## Having your work marked

There is no answer file and no test here, on purpose. On the [MitsuruTech Learning Platform](https://mitsurutech.co.uk/learning) a teacher can set this task for a class and have it marked for them. A college account is [free for the first year](https://mitsurutech.co.uk/pricing) for up to 50 students.

[All Python exercises](../../../README.md)

Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) by Mitsuru Technologies Ltd.

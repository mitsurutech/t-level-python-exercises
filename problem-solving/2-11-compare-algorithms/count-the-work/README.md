# Count the work: Python exercise for T Level Digital Software Development

> **From the lesson:** [2.11: Comparing algorithms](https://mitsurutech.co.uk/resources/t-level/dsd-2-11-compare-algorithms)

## What to do

Count the work of linear search and binary search. The tests need an exact count, so follow these rules.

1. `count_linear(items, target)` counts the items compared with the target before the search stops.
2. `count_binary(items, target)` counts the middle items looked at, with the middle index `(low + high) // 2`. Each middle item counts as 1, even if you test it with both == and <.
3. `best_case_target(items)` gives back the item a linear search finds with the fewest comparisons.
4. `worst_case_target(items)` gives back the item it finds with the most.

## Starter files

- `main.py`

Write your answer in `main.py`. To try it, add a few `print(...)` lines at the bottom and run `python3 main.py`.

## Stuck?

Read the free [lesson preview](https://mitsurutech.co.uk/resources/t-level/dsd-2-11-compare-algorithms), which explains the idea and lets you try its first activities. All the lessons have [free previews](https://mitsurutech.co.uk/resources/t-level).

## Having your work marked

There is no answer file and no test here, on purpose. On the [MitsuruTech Learning Platform](https://mitsurutech.co.uk/learning) a teacher can set this task for a class and have it marked for them. A college account is [free for the first year](https://mitsurutech.co.uk/pricing) for up to 50 students.

[All Python exercises](../../../README.md)

Licensed under [CC BY-NC-SA 4.0](https://creativecommons.org/licenses/by-nc-sa/4.0/) by Mitsuru Technologies Ltd.

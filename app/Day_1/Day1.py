from app.file_paths import day1_file

with open(day1_file) as day_1:
    nums = [int(line) for line in day_1]
# -------------------------------------------------------------------------------------------------------
# Part 1


def product_numbers(num):
    for x in num:
        if (2020 - x) in num:
            return (2020 - x) * x
# -------------------------------------------------------------------------------------------------------
# Part 2


def product_of_three(num):
    for x in num:
        for y in num:
            if (2020 - (x + y)) in num:
                return (2020 - (x + y)) * x * y






from app.file_paths import day1_file as file
# -------------------------------------------------------------------------------------------------------
# Function to read input file


def read(path):
    with open(path, 'r') as day_1:
        nums = [int(line) for line in day_1]
    return nums
# -------------------------------------------------------------------------------------------------------
# Day 1 Part 1


def product_numbers():
    num = read(file)
    for x in num:
        if (2020 - x) in num:
            return (2020 - x) * x
# -------------------------------------------------------------------------------------------------------
# Day 1 Part 2


def product_of_three():
    num = read(file)
    for x in num:
        for y in num:
            if (2020 - (x + y)) in num:
                return (2020 - (x + y)) * x * y

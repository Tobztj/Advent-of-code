with open('Day1_input.txt') as day_1:
    nums = [int(line) for line in day_1]
# -------------------------------------------------------------------------------------------------------
# Part 1


def product_numbers(nums):
    for x in nums:
        if (2020 - x) in nums:
            return (2020 - x) * x
# -------------------------------------------------------------------------------------------------------
# Part 2


def product_of_three(nums):
    for x in nums:
        for y in nums:
            if (2020 - (x + y)) in nums:
                return (2020 - (x + y)) * x * y
# -------------------------------------------------------------------------------------------------------
# function to run file


def run():
    print(product_numbers(nums))
    print(product_of_three(nums))


if __name__ == '__main__':
    run()

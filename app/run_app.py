# -------------------------------------------------------------------------------------------------------
# function to run all files
from app.Day_1.Day1 import *
from app.Day_2.Day2 import *


def run():
    print(f'Day 1: \n'
          f'Part 1 --> {product_numbers(nums)} \n'
          f'Part 2 --> {product_of_three(nums)}')
    print(f'Day 2: \n'
          f'Part 1 --> {valid_passwords()} \n'
          f'Part 2 --> {password_count()}')
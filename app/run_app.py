# -------------------------------------------------------------------------------------------------------
# function to run all files
from app.Day_1.Day1 import *
from app.Day_2.Day2 import *
from app.Day_3.Day3 import *


def run():
    print(f'Day 1: \n'
          f'Part 1 --> Product of two numbers that sum to 2020 is {product_numbers()} \n'
          f'Part 2 --> Product of three numbers that sum to 2020 is {product_of_three()}')
    print(f'Day 2: \n'
          f'Part 1 --> There are {valid_passwords()} valid passwords \n'
          f'Part 2 --> There are {password_count()} valid passwords, for the new password policy')
    print(f'Day 3: \n'
          f'Part 1 --> There are {number_of_trees()} trees \n'
          f'Part 2 --> The product of the number of trees for each slope is {multiple_trees()}')
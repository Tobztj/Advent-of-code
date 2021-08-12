# -------------------------------------------------------------------------------------------------------
# Day 4 Part 2 again using separate functions for validate each field within the passports
from app.Day_4.Day4 import all_passports, is_valid_passport


def valid_dates(passports):
    # Function to validate the date fields
    birth_year = 1920 <= int(passports['byr']) <= 2002
    issue_year = 2010 <= int(passports['iyr']) <= 2020
    expiration_year = 2020 <= int(passports['eyr']) <= 2030
    return birth_year and issue_year and expiration_year


def valid_height(passports):
    # Function to validate the height field
    valid = False
    if passports['hgt'].isalnum():
        if passports['hgt'][-2:] == 'cm':
            height = int(passports['hgt'][0:-2])
            valid = 150 <= height <= 193
        elif passports['hgt'][-2:] == 'in':
            height = int(passports['hgt'][0:-2])
            valid = 59 <= height <= 76
    return valid


def valid_hcl(passports):
    # Function to validate the hair color field
    valid = False
    hair_color = passports['hcl']
    if len(hair_color) == 7 and hair_color[0] == '#':
        valid = True
        for char in hair_color[1:]:
            if char not in "0123456789abcdef":
                valid = False
    return valid


def valid_ecl(passports):
    # Function to validate the eye color field
    for color in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        if passports['ecl'] in color:
            return True


def valid_pid(passports):
    # Function to validate the passport identification number field
    if len(passports['pid']) == 9:
        return True


def valid_fields(passports):
    # Function to call and run all validations
    valid_h = valid_height(passports)
    dates = valid_dates(passports)
    valid_ec = valid_ecl(passports)
    valid_hc = valid_hcl(passports)
    valid_pi = valid_pid(passports)
    return valid_pi and valid_h and dates and valid_hc and valid_ec


def total_validated_passports():
    # Function to count the total number of validated passports
    valid_passport = [passport for passport in all_passports() if is_valid_passport(passport)]
    validated_passports = [passport for passport in valid_passport if valid_fields(passport)]
    return len(validated_passports)




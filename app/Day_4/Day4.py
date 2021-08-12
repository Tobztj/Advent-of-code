from app.file_paths import day4_file as file
# -------------------------------------------------------------------------------------------------------
# Function to read text file


def read(txt_file):
    day4 = open(txt_file, 'r').read()
    lines = day4.split("\n\n")
    line = [line.replace("\n", " ") for line in lines]
    line_split = [new_line.split() for new_line in line]
    return line_split


def dictionary_converter(items):
    user = {}
    for item in items:
        item_part = item.split(":")
        key = item_part[0]
        value = item_part[1]
        user[key] = value
    return user


def all_passports():
    passports = [dictionary_converter(details) for details in read(file)]
    return passports
# -------------------------------------------------------------------------------------------------------
# Day 4 Part 1


def is_valid_passport(each_passport):
    has_birth_year = "byr" in each_passport
    has_issue_year = "iyr" in each_passport
    has_expiration_year = "eyr" in each_passport
    has_height = "hgt" in each_passport
    has_hair_color = "hcl" in each_passport
    has_eye_color = "ecl" in each_passport
    has_passport_id = "pid" in each_passport
    has_country_id = "cid" in each_passport

    return (
            has_birth_year and
            has_issue_year and
            has_expiration_year and
            has_height and
            has_hair_color and
            has_eye_color and
            has_passport_id
    )


valid_passport = [passport for passport in all_passports() if is_valid_passport(passport)]
# -------------------------------------------------------------------------------------------------------
# Day 4 Part 2


def valid_fields(passports):
    birth_year = 1920 <= int(passports['byr']) <= 2002
    issue_year = 2010 <= int(passports['iyr']) <= 2020
    expiration_year = 2020 <= int(passports['eyr']) <= 2030
    valid_height = False
    if passports['hgt'].isalnum():
        if passports['hgt'][-2:] == 'cm':
            height = int(passports['hgt'][0:-2])
            valid_height = 150 <= height <= 193
        elif passports['hgt'][-2:] == 'in':
            height = int(passports['hgt'][0:-2])
            valid_height = 59 <= height <= 76

    valid_hair_color = False
    hair_color = passports['hcl']
    if len(hair_color) == 7 and hair_color[0] == '#':
        valid_hair_color = True
        for char in hair_color[1:]:
            if char not in "0123456789abcdef":
                valid_hair_color = False

    valid_eye_color = False
    if passports['ecl'] in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        valid_eye_color = True

    valid_pid = False
    if len(passports['pid']) == 9:
        valid_pid = True

    return (
            birth_year and issue_year
            and expiration_year and valid_height
            and valid_hair_color and valid_eye_color
            and valid_pid
            )


validated_passports = [passport for passport in valid_passport if valid_fields(passport)]
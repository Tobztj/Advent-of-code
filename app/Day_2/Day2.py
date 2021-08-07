from app.file_paths import day2_file as file
# -------------------------------------------------------------------------------------------------------
# Function to read text file


def read_file(path):
    with open(path, 'r') as day_2:
        lines = [line.rstrip() for line in day_2]
        new_lines = []
        chars = ['-', ':']
        for line in lines:
            for char in chars:
                line = line.replace(char, ' ')
            line = line.split(" ")
            new_lines.append(line)
    return new_lines
# -------------------------------------------------------------------------------------------------------
# Day 2 part 1


def valid_passwords():
    number_of_valid_passwords = []
    for line in read_file(file):
        count = line[4].count(line[2])
        counter = 0
        if int(line[0]) <= count <= int(line[1]):
            counter += 1
        if counter == 1:
            number_of_valid_passwords.append(counter)
    return len(number_of_valid_passwords)
# -------------------------------------------------------------------------------------------------------
# Day 2 part 2


def password_count():
    valid_password = []
    for line in read_file(file):
        v1, v2 = int(line[0]), int(line[1])
        count = 0
        if line[4][v1-1] == line[2]:
            count += 1
        if line[4][v2-1] == line[2]:
            count += 1
        if count == 1:
            valid_password.append(count)
    return len(valid_password)


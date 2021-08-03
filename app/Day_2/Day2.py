from app.file_paths import day2_file
# -------------------------------------------------------------------------------------------------------
# Day 2 part 1


def valid_passwords():
    day_2 = open(day2_file, 'r')
    number = 0
    for line in day_2:
        line = line.rstrip()
        chars = ['-', ':']
        for char in chars:
            line = line.replace(char, ' ')
        line = line.split(" ")
        count = line[4].count(line[2])
        if int(line[0]) <= count <= int(line[1]):
            number += 1
    #print(number)
    return number


# -------------------------------------------------------------------------------------------------------
# Day 2 part 2


def password_count():
    day_2 = open(day2_file, 'r')
    valid_password = []
    for line in day_2:
        line = line.rstrip()
        chars = ['-', ':']
        for char in chars:
            line = line.replace(char, ' ')
        line = line.split(" ")
        v1, v2 = int(line[0]), int(line[1])
        count = 0
        if line[4][v1-1] == line[2]:
            count += 1
        if line[4][v2-1] == line[2]:
            count += 1
        if count == 1:
            valid_password.append(count)
    return len(valid_password)






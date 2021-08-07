from app.file_paths import day3_file as file
# -------------------------------------------------------------------------------------------------------
# Function to read text file


def read(path):
    day3 = open(path, 'r').read().strip()
    lines = day3.splitlines()
    return lines
# -------------------------------------------------------------------------------------------------------
# Day 3 Part 1


def number_of_trees():
    trees = 0
    lines = read(file)
    right, down = 0, 0
    while down+1 < len(lines):
        right += 3
        down += 1
        space = lines[down][right % len(lines[down])]
        if space == '#':
            trees += 1
    return trees
# -------------------------------------------------------------------------------------------------------
# Day 3 Part 2


def multiple_trees():
    trees = []
    lines = read(file)
    product_trees = 1
    slopes = [[1, 1], [3, 1], [5, 1], [7, 1], [1, 2]]
    for slope in slopes:
        count = 0
        right, down = 0, 0
        while down+1 < len(lines):
            right += slope[0]
            down += slope[1]
            space = lines[down][right % len(lines[down])]
            if space == '#':
                count += 1
        trees.append(count)
    for tree in trees:
        product_trees *= tree
    return product_trees

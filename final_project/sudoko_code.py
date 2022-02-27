from random import sample

base = 3
side = base * base


# pattern for a baseline valid solution
def pattern(r, c):
    return (base * (r % base) + r // base + c) % side


# randomize rows, columns and numbers (of valid base pattern)
def shuffle(s):
    return sample(s, len(s))


# produce board using randomized baseline pattern
def generate_sudoku():
    rBase = range(base)
    rows = [g * base + r for g in shuffle(rBase) for r in shuffle(rBase)]
    cols = [g * base + c for g in shuffle(rBase) for c in shuffle(rBase)]
    nums = shuffle(range(1, base * base + 1))
    return [[nums[pattern(r, c)] for c in cols] for r in rows]


def is_sudoku_valid(grid):
    for row in range(len(grid)):
        for col in range(len(grid)):
            # check value is an int
            if grid[row][col] < 1 or type(grid[row][col]) is not type(1):
                return False
            # check value is within 1 through n.
            # for example a 2x2 grid should not have the value 8 in it
            elif grid[row][col] > len(grid):
                return False
    # check the rows
    for row in grid:
        if sorted(list(set(row))) != sorted(row):
            return False
    # check the cols
    cols = []
    for col in range(len(grid)):
        for row in grid:
            cols += [row[col]]
        # set will get unique values, its converted to list so you can compare
        # it's sorted so the comparison is done correctly.
        if sorted(list(set(cols))) != sorted(cols):
            return False
        cols = []
    # if you get past all the false checks return True
    return True



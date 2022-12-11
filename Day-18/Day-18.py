# Advent of Code 2016, Day-18
# https://adventofcode.com/2016
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

TOTAL_ROW_1 = 40
TOTAL_ROW_2 = 400000
# TOTAL_ROW_1 = 10  # test data

# Patterns that will generate a trap '^' in the new spot
traps = (
    '^^.',
    '.^^',
    '^..',
    '..^'
)


def next_row(this_row):
    row = ''
    this_row = '.' + this_row + '.'  # padding of safe spots at both ends of the string
    for i in range(1, len(this_row) - 1):
        if this_row[i - 1:i + 2:] in traps:
            row += '^'
        else:
            row += '.'
    return row


def count_safe(row):
    return row.count('.')


def solve_1(this_row, number_of_rows):
    number_safe_spots = count_safe(this_row)
    for i in range(number_of_rows - 1):  # -1 since the first row is the input
        # print(f'{this_row} safe = {number_safe_spots}')
        new_row = next_row(this_row)
        number_safe_spots += count_safe(new_row)
        this_row = new_row
    return number_safe_spots


def main():
    with open('Day-18-data.txt', 'r') as f:
        # input_data = f.readlines()
        input_line = f.read().strip()

    print(f'Day 18, Part 1--Number of safe spots for {TOTAL_ROW_1} rows is {solve_1(input_line, TOTAL_ROW_1)}')
    print(f'Day 18, Part 2--Number of safe spots for {TOTAL_ROW_2} rows is {solve_1(input_line, TOTAL_ROW_2)}')


if __name__ == '__main__':
    main()

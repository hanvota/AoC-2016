# Advent of Code 2016, Day-03
# https://adventofcode.com/2016
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import re

pattern = r'(\d+) +(\d+) +(\d+)'


def is_valid_triangle(a, b, c):  # returns 1 if triangle is valid, otherwise 0

    if (a + b <= c) or (a + c <= b) or (b + c <= a):
        return 0
    return 1


def solve_part_1(inputs):
    count = 0
    for input_line in inputs:
        result = re.search(pattern, input_line.strip().rstrip())
        a = int(result[1])
        b = int(result[2])
        c = int(result[3])

        count += is_valid_triangle(a, b, c)

    print(f'Day 03, Part 1--{count} triangles are possible')


def solve_part_2(inputs):
    count = 0
    for i in range(0, len(inputs), 3):
        m = []
        for j in range(3):
            line = (inputs[i + j].strip().rstrip())
            result = re.search(pattern, line)
            m.append([int(result[1]), int(result[2]), int(result[3])])

        for j in range(3):
            a = m[0][j]
            b = m[1][j]
            c = m[2][j]
            count += is_valid_triangle(a, b, c)

    print(f'Day 03, Part 2--{count} triangles are possible')


if __name__ == '__main__':
    with open('Day-03-data.txt', 'r') as f:
        input_data = f.readlines()

    solve_part_1(input_data)
    solve_part_2(input_data)

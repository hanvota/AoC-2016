# Advent of Code 2016, Day-15
# https://adventofcode.com/2016
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import re
from collections import deque

pattern = r'.*#(\d+) has (\d+).*position.(\d+)'
EXTRA_DISC_SIZE = 11
discs = {}


def setup_discs(input_data):
    for input_line in input_data:
        m = re.search(pattern, input_line.strip())
        # print(f'Disc {m[1]}, length {m[2]} at position {m[3]}')
        discs[m[1]] = deque([x for x in range(int(m[2]))])
        discs[m[1]].rotate(int(m[3]))


def bounce(level):  # True if the capsule bounces at this level (if position '0' not at the front)
    return discs[level][0] != 0


def show_discs():
    for key, value in discs.items():
        print(f'Disc #{key}, position {value[0]}, status {value}')


def rotate_discs(count):
    for i in range(1, len(discs) + 1):
        # print(discs[str(i)])
        discs[str(i)].rotate(count)
    pass


def solve(input_data, part2):
    start_time = -1
    found = False
    extra_disc = 0
    while not found:
        setup_discs(input_data)
        if part2 and extra_disc == 0:
            extra_disc = str(len(discs) + 1)
            discs[extra_disc] = deque([x for x in range(EXTRA_DISC_SIZE)])
            discs[extra_disc].rotate(-1)

        print('\nReset discs')
        if start_time >= 0:
            print('Rotate to appropriate position')
            rotate_discs(start_time + 1)
        show_discs()
        start_time += 1
        print(f'Start time={start_time}')
        for level in range(len(discs)):
            print(f'Level {level + 1}')
            rotate_discs(1)
            show_discs()
            if bounce(str(level + 1)):
                print(f'Bounce on level {level + 1}')
                break
        else:  # here is capsule can pass thru all levels
            found = True

        # if part2 and start_time > 9:
        #     show_discs()
        #     break

    return start_time


def main():
    with open('Day-15-data.txt', 'r') as f:
        input_data = f.readlines()

    print(f'Day 15, Part 1--Push the button at time {solve(input_data, part2=False)}')
    print(f'Day 15, Part 2--Push the button at time {solve(input_data, part2=True)}')


if __name__ == '__main__':
    main()

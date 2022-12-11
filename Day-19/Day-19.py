# Advent of Code 2016, Day-19
# https://adventofcode.com/2016
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import collections
from time import perf_counter
import time

PUZZLE_INPUT = 3014603


# PUZZLE_INPUT = 5


def convert(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))


def solve_1(number_of_elves):  # Elves steal presents from his/her adjacent left side
    circle_of_elves = [[x, 1] for x in range(1, number_of_elves + 1)]  # [[elf_number, number of presents], [next_elf_number, number of presents]....]
    # print(circle_of_elves)
    i = 0
    while len(circle_of_elves) > 1:
        print(i, '- ', circle_of_elves[i][0], 'takes from ', circle_of_elves[(i + 1) % len(circle_of_elves)][0])
        circle_of_elves[i][1] += circle_of_elves[(i + 1) % len(circle_of_elves)][1]
        circle_of_elves.remove(circle_of_elves[(i + 1) % len(circle_of_elves)])
        # print(circle_of_elves)
        if i == len(circle_of_elves):
            i = 0
        else:
            i = (i + 1) % len(circle_of_elves)

    return circle_of_elves[0]


def solve_2(number_of_elves):  # # Elves steal presents one who is across from the circle, left side one if more than 1 choice
    circle_of_elves = [[x, 1] for x in range(1, number_of_elves + 1)]  # [[elf_number, number of presents], [next_elf_number, number of presents]....]
    # print(circle_of_elves)
    i = 0
    while len(circle_of_elves) > 1:
        elf_across = int((len(circle_of_elves) / 2))
        print(i, '- ', circle_of_elves[i][0], 'takes from ', circle_of_elves[(i + elf_across) % len(circle_of_elves)][0])
        circle_of_elves[i][1] += circle_of_elves[(i + elf_across) % len(circle_of_elves)][1]
        circle_of_elves.remove(circle_of_elves[(i + elf_across) % len(circle_of_elves)])
        # print(circle_of_elves)
        if i == len(circle_of_elves):
            i = 0
        else:
            i = (i + 1) % len(circle_of_elves)

    return circle_of_elves[0]


def solve_parttwo():
    left = collections.deque()
    right = collections.deque()
    for i in range(1, PUZZLE_INPUT + 1):
        if i < (PUZZLE_INPUT // 2) + 1:
            left.append(i)
        else:
            right.appendleft(i)

    while left and right:
        if len(left) > len(right):
            left.pop()
        else:
            right.pop()

        # rotate
        right.appendleft(left.popleft())
        left.append(right.pop())
    return left[0] or right[0]


def main():
    # t1_start = perf_counter()
    # last_elf = solve_1(PUZZLE_INPUT)
    # print(f'Day 19, Part 1--Elf number {last_elf[0]} gets all {last_elf[1]} presents ')
    # t1_stop = perf_counter()
    # print(f'Elapsed time for part 1 (in seconds): {convert(int(t1_stop - t1_start))}')
    # print()
    t1_start = perf_counter()
    # last_elf = solve_2(PUZZLE_INPUT)
    last_elf = solve_parttwo()
    # print(f'Day 19, Part 2--Elf number {last_elf[0]} gets all {last_elf[1]} presents ')
    print(f'Day 19, Part 2--Elf number {last_elf} gets all the presents')
    t1_stop = perf_counter()
    print(f'Elapsed time for part 1 (in seconds): {convert(int(t1_stop - t1_start))}')


if __name__ == '__main__':
    main()

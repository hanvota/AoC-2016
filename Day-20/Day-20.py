# Advent of Code 2016, Day-20
# https://adventofcode.com/2016
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

import collections
from time import perf_counter
import time


def convert(seconds):
    return time.strftime("%H:%M:%S", time.gmtime(seconds))


def solve(input):
    ip_addresses = collections.deque(range(2 ** 32))
    for input_line in input:
        # print(f'{input_line}')
        from_ip, to_ip = input_line.strip().split('-')
        print(from_ip, to_ip)
        for ip in range(int(from_ip), int(to_ip)):
            ip_addresses.remove(ip)
    return ip_addresses[0]


def main():
    with open('Day-20-data.txt', 'r') as f:
        input_data = f.readlines()
        # input_data = f.read().strip()

    t1_start = perf_counter()
    lowest_ip = solve(input_data)
    print(f'Day 20, Part 1--Lowest IP address is {lowest_ip}')
    t1_stop = perf_counter()
    print(f'Elapsed time for part 1 (in seconds): {convert(int(t1_stop - t1_start))}')

    # print(f'Day 20, Part 2--')


if __name__ == '__main__':
    main()

# Advent of Code 2016, Day-09
# https://adventofcode.com/2016
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import re

pattern = r'\((\d+)x(\d+)\)'


def decompress_1(in_line):
    decoded_line = ''
    while in_line != '':
        m = re.search(pattern, in_line)
        if m is None:
            break
        s = m.span(0)
        num_chars = int(m.group(1))
        repeats = int(m.group(2))
        repeat_seg = in_line[s[1]:s[1] + num_chars]

        decoded_line += in_line[:s[0]] + repeat_seg * repeats
        in_line = in_line[s[1] + num_chars:]

    num_spaces = decoded_line.count(' ')
    length = len(decoded_line) - num_spaces

    return length


def decompress_2(in_line):
    stack = []
    decoded_line = ''

    def process_stack():
        nonlocal stack
        nonlocal decoded_line
        nonlocal in_line
        segment = ''
        reps = 1
        while stack:
            command = stack.pop()
            reps *= command[1]  # number of repeats is a multiplication of all the repeats on the stack
            if segment == '':
                segment = in_line[:command[0]]
                in_line = in_line[command[0]:]

        decoded_line += segment * reps

    while in_line != '':
        m = re.search(pattern, in_line)
        if m is not None:
            s = m.span(0)
            num_chars = int(m.group(1))
            repeats = int(m.group(2))

        if in_line[0] == '(':  # in the next char is '(' we have another decoding instruction
            stack.append((num_chars, repeats))  # will stack this command for now
            in_line = in_line[s[1]:]
        else:  # we have a stack of instructions to go thru
            process_stack()
            if m is not None:
                decoded_line += in_line[:s[0]]
                in_line = in_line[s[0]:]
            else:
                decoded_line += in_line[:]
                in_line = ''
    num_spaces = decoded_line.count(' ')
    length = len(decoded_line) - num_spaces
    return length


def part_1(input_data):
    length = 0
    for input_line in input_data:
        # print(f'{input_line}')
        length = decompress_1(input_line.strip())

    return length


def part_2(input_data):
    length = 0
    for input_line in input_data:
        # print(f'{input_line}')
        length = decompress_2(input_line.strip())

    return length


if __name__ == '__main__':
    with open('Day-09-data.txt', 'r') as f:
        input_data = f.readlines()

    print(f'Day 09, Part 1--Decompressed length of the file is {part_1(input_data)}')
    print(f'Day 09, Part 2--Decompressed length of the improved format is {part_2(input_data)}')

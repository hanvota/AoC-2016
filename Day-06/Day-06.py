# Advent of Code 2016, Day-06
# https://adventofcode.com/2016
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from operator import itemgetter


def requested_letters(data, col):  # find the most freq letter at the position indicated
    letter_freq = {}
    for line in data:
        c = line[col]
        if c not in letter_freq.keys():
            letter_freq[c] = 1
        else:
            letter_freq[c] += 1

    letter_freq = dict(sorted(letter_freq.items(), key=itemgetter(1), reverse=True))  # sort by value (number of occurrence)
    most_common_char = list(letter_freq.keys())[0]  # 1st item is the most common
    least_common_char = list(letter_freq.keys())[-1]  # last item is the least common
    return most_common_char, least_common_char


def process(data):
    part_1_message = ''
    part_2_message = ''

    msg_length = len(data[0]) - 1  # except the last '\n'
    for pos in range(msg_length):
        most_common_char, least_common_char = requested_letters(data, pos)
        part_1_message += most_common_char
        part_2_message += least_common_char
    return part_1_message, part_2_message


if __name__ == '__main__':
    with open('Day-06-data.txt', 'r') as f:
        input_data = f.readlines()

    part_1_message, part_2_message = process(input_data)
    print(f'Day 06, Part 1--Error corrected message is "{part_1_message}"')
    print(f'Day 06, Part 2--Original message is "{part_2_message}"')

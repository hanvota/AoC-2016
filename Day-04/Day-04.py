# Advent of Code 2016, Day-04
# https://adventofcode.com/2016
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
from operator import itemgetter


def calc_checksum(letters):
    word = letters.keys()
    return ''.join(word)[:5]


def encrypt_name(name):  # True is it is real room
    letters_dict = {}
    for c in name:
        if c == '-':
            continue
        else:
            if c not in letters_dict:       # found new letter
                letters_dict[c] = 1
            else:
                letters_dict[c] += 1
    letters_dict = dict(sorted(letters_dict.items()))  # 1st sort the key (letters)
    letters_dict = dict(sorted(letters_dict.items(), key=itemgetter(1), reverse=True))  # 2nd sort by value (number of occurrence
    return calc_checksum(letters_dict)


letters = 'abcdefghijklmnopqrstuvwxyz'          # used for rotation of letters


def rotate(c, number):
    position = letters.find(c)
    return letters[(position + number) % len(letters)]


def decrypt_name(name, rotations):
    name_list = list(name)
    for i in range(len(name_list)):
        c = name_list[i]
        if c == '-':
            c = ' '
        else:
            c = rotate(c, rotations)
        name_list[i] = c
    return ''.join(name_list)


def separate_items(input):
    name = input[:-12]
    sector = int(input[-11:-8])
    checksum = input[-7:-2]
    return name, sector, checksum


def part_2(data):
    for input_line in data:
        room_name, sector_id, checksum = separate_items(input_line)
        if encrypt_name(room_name) == checksum:                     # 1st find the 'real' rooms from decoy (from part 1)
            if decrypt_name(room_name, sector_id).find('northpole object') != -1:       # then look for the name
                return sector_id
    return 0


def part_1(data):
    sum_of_sector_ids = 0
    for input_line in data:
        room_name, sector_id, checksum = separate_items(input_line)
        if encrypt_name(room_name) == checksum:
            sum_of_sector_ids += sector_id

    return sum_of_sector_ids


if __name__ == '__main__':
    with open('Day-04-data.txt', 'r') as f:
        input_data = f.readlines()

    print(f'Day 04, Part 1--Result is {part_1(input_data)}')
    print(f'Day 04, Part 2--Sector ID of room is {part_2(input_data)}')
#

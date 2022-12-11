# Advent of Code 2016, Day-07
# https://adventofcode.com/2016
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import re


def has_ABBA(word):
    return any(a != b for a, b in re.findall(r'(.)(.)\2\1', word))


def has_ABA_and_BAB(hypernet, supernet):
    return re.findall(r'(.)(.)\1.*X.*\2\1\2', hypernet + "X" + supernet)


def is_valid_1(line):
    ip = []  # contains the ip, without portion in [....]
    while True:
        loc1 = line.find('[')
        if loc1 == -1:  # no more '['
            break

        loc2 = line.find(']')
        word = line[loc1 + 1:loc2]  # look for word(s) in []
        if has_ABBA(word):  # if any of them has ABBA, then not valid
            return False
        ip.append(line[:loc1])  # part before [
        line = line[loc2 + 1:]  # delete the used portion

    # print()
    ip.append(line)  # the remaining portion of the IP, after the last ']'
    # process the remaining word list
    # if ip has ABBA then is valid
    for i in ip:
        if has_ABBA(i):
            return True

    return False


def is_valid_2(line):
    supernet = ''  # contains the ip, without portion in [....]
    hypernet = ''
    while True:
        loc1 = line.find('[')
        if loc1 == -1:  # no more '['
            break
        loc2 = line.find(']')
        hypernet = hypernet + '  ' + line[loc1 + 1:loc2]  # collect the hypernet (inside []) segments together, separated by ' '
        supernet = supernet + '  ' + line[:loc1]  # collect the supernet (outside []) segments together, separated by ' '
        line = line[loc2 + 1:]  # delete the used portion

    supernet = supernet + '  ' + line  # the remaining portion of the IP, after the last ']'

    # want ABA in supernet AND BAB in hypernet AND A != B
    p = has_ABA_and_BAB(hypernet.lstrip(), supernet.lstrip())  # ABA and BAB
    if p != []:
        return True
    else:
        return False


def part_1(data):
    valid = 0
    for input_line in data:
        if is_valid_1(input_line.strip()):
            valid += 1

    return valid


def part_2(data):
    valid = 0
    for input_line in data:
        if is_valid_2(input_line.strip()):
            valid += 1

    return valid


if __name__ == '__main__':
    with open('Day-07-data.txt', 'r') as f:
        input_data = f.readlines()

    print(f'Day 07, Part 1-- {part_1(input_data)} IPs support TLS')
    print(f'Day 07, Part 2-- {part_2(input_data)} IPs support SSL')

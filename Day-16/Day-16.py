# Advent of Code 2016, Day-16
# https://adventofcode.com/2016
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

PUZZLE_INPUT = '10111011111001111'
# CHECK_RESULT = '1111000010100101011110000'
DISK_LENGTH_1 = 272
DISK_LENGTH_2 = 35651584


def inverse(input):
    result = ''
    for i in input:
        if i == '1':
            result += '0'
        else:
            result += '1'
    return result


def generate_code(a):
    b = a[::-1]  # b = reverse of a
    b = inverse(b)  # flip all the 'bits'
    result = a + '0' + b
    return result


def next_checksum(input):
    result = ''
    for i in range(0, len(input) - 1, 2):
        if input[i] == input[i + 1]:
            result += '1'
        else:
            result += '0'
    return result


def generate_checksum(checksum):
    while len(checksum) % 2 == 0:  # repeat until length is odd
        checksum = next_checksum(checksum)
    return checksum


def solve(length):
    a = PUZZLE_INPUT
    code = ''
    while len(code) < length:
        code = generate_code(a)
        a = code
    code = code[:length]
    checksum = generate_checksum(code)
    return checksum


def main():
    print(f'Day 16, Part 1--Checksum for disk length {DISK_LENGTH_1} is {solve(DISK_LENGTH_1)}')
    print(f'Day 16, Part 2--Checksum for for disk length {DISK_LENGTH_2} is {solve(DISK_LENGTH_2)}')


if __name__ == '__main__':
    main()

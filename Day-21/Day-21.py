# Advent of Code 2016, Day-21
# https://adventofcode.com/2016
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from itertools import permutations

START_PW = 'abcdefgh'
END_PW = 'fbgdceah'


# START_PW = 'abcde'  # test data


def do_swap(pw, instruction):
    if instruction[1] == 'position':
        fro_ = int(instruction[2])
        to_ = int(instruction[-1])
    elif instruction[1] == 'letter':
        fro_ = pw.index(instruction[2])
        to_ = pw.index(instruction[-1])
    else:
        print(f'Unknown swap {instruction[1]}')
        return pw
    temp = pw[fro_]
    pw[fro_] = pw[to_]
    pw[to_] = temp

    return pw


def do_reverse(pw, instruction):
    fro_ = int(instruction[2])
    to_ = int(instruction[4])
    beginning = pw[:fro_]
    substring = pw[fro_:to_ + 1]
    end = pw[to_ + 1:]
    substring = substring[::-1]
    pw = beginning + substring + end

    return pw


def do_rotate(pw, instruction):
    if instruction[1] == 'based':
        count = pw.index(instruction[-1])
        if count >= 4:
            count += 1
        count += 1
        for _ in range(count):
            pw = list(pw[-1]) + pw[:-1]
    elif instruction[1] == 'left':
        count = int(instruction[2])
        for _ in range(count):
            pw = pw[1:] + list(pw[0])
    elif instruction[1] == 'right':
        count = int(instruction[2])
        for _ in range(count):
            pw = list(pw[-1]) + pw[:-1]
    else:
        print(f'Unknown swap {instruction[1]}')

    return pw


def do_move(pw, instruction):
    fro_ = int(instruction[2])
    to_ = int(instruction[-1])
    temp = pw.pop(fro_)
    pw.insert(to_, temp)
    return pw


def solve_1(pw, instructions):
    # print(pw)
    for line in instructions:
        # print(f'{line}')
        instruction = line.split()
        # print(instruction)
        if instruction[0] == 'swap':
            pw = do_swap(pw, instruction)
        elif instruction[0] == 'reverse':
            pw = do_reverse(pw, instruction)
        elif instruction[0] == 'rotate':
            pw = do_rotate(pw, instruction)
        elif instruction[0] == 'move':
            pw = do_move(pw, instruction)
        else:
            print(f'Unknown command {instruction[0]}')
    return "".join(pw)


def solve_2(start_pw, goal_pw, instructions):
    for perm in permutations("".join(start_pw)):
        pw = solve_1(list(perm), instructions)
        # print(f'{"".join(perm)} -> {pw}')
        if pw == goal_pw:
            return "".join(perm)


def main():
    with open('Day-21-data.txt', 'r') as f:
        input_data = f.readlines()
        # input_data = f.read().strip()

    pw = solve_1(list(START_PW), input_data)
    print(f'Day 21, Part 1--Scrambled password is {pw}')

    pw = solve_2(list(START_PW), END_PW, input_data)
    print(f'Day 21, Part 2--Un-Scrambled password is {pw}')


if __name__ == '__main__':
    main()

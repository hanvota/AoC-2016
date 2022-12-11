# Advent of Code 2016, Day-12
# https://adventofcode.com/2016
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

def run(program, part=1):
    registers = {
        'a': 0,
        'b': 0,
        'c': 0,
        'd': 0
    }
    if part == 2:
        registers['c'] = 1
    regs = set(registers.keys())
    pc = 0  # program counter
    eof = len(program)  # end of program
    while pc < eof:
        parse_line = program[pc].split(' ')
        # print(f'{parse_line}')
        cmd = parse_line[0]
        if cmd == 'cpy':
            if parse_line[1] in regs:
                registers[parse_line[2]] = registers[parse_line[1]]
            else:
                registers[parse_line[2]] = int(parse_line[1])
        elif cmd == 'inc':
            registers[parse_line[1]] += 1
        elif cmd == 'dec':
            registers[parse_line[1]] -= 1
        elif cmd == 'jnz':
            if parse_line[1] in regs:
                comparator = registers[parse_line[1]]
            else:
                comparator = int(parse_line[1])
            if comparator != 0:
                if parse_line[1] in regs:
                    offset = registers[parse_line[1]]
                else:
                    offset = int(parse_line[1])
                pc += offset
                continue
        else:
            print(f'Unknown instruction {parse_line}')
        pc += 1
    return registers['a']


def main():
    # with open('Day-12-data.txt', 'r') as f:
    #     input_data = f.readlines()

    with open('Day-12-data.txt') as file:
        data = [i for i in file.read().strip().split("\n")]

    print(f'Day 12, Part 1--Register a has value {run(data, 1)}')
    print(f'Day 12, Part 2--Register a has value {run(data, 2)}')


if __name__ == '__main__':
    main()

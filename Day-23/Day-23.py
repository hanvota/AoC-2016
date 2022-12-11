# Advent of Code 2016, Day-23
# https://adventofcode.com/2016
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.


def run(program, part=1):
    registers = {
        'a': 7,
        'b': 0,
        'c': 0,
        'd': 0
    }
    replace_instruction = {  # the replacement instructions for the 'tgl' commands
        'cpy': 'jnz',
        'jnz': 'cpy',
        'inc': 'dec',
        'dec': 'inc',
        'tgl': 'inc'
    }

    def fetch(from_):  # get the value (either an immediate value or content of a register
        if from_ in regs:
            return registers[from_]
        else:
            return int(from_)

    if part == 2:
        registers['c'] = 1
    regs = set(registers.keys())
    pc = 0  # program counter
    eof = len(program)  # end of program
    while pc < eof:
        parse_line = program[pc].split(' ')
        print(f'{parse_line}')
        cmd = parse_line[0]
        # try:
        if cmd == 'cpy':
            registers[parse_line[2]] = fetch(parse_line[1])
        elif cmd == 'inc':
            registers[parse_line[1]] += 1
        elif cmd == 'dec':
            registers[parse_line[1]] -= 1
        elif cmd == 'jnz':
            comparator = fetch(parse_line[1])
            if comparator != 0:
                offset = fetch(parse_line[2])
                pc += offset
                continue
        elif cmd == 'tgl':
            dest = pc + int(registers[parse_line[1]])
            if 0 <= dest < eof:  # only perform command if in range, nothing happens
                original_instruction = program[dest]
                new_instruction = replace_instruction[original_instruction[:3]]
                program[dest] = new_instruction + original_instruction[3:]
        else:
            print(f'Unknown instruction {parse_line}')
        # except KeyError:  # skip invalid instructions
        #     pass

        pc += 1

    return registers['a']


def main():
    with open('Day-23-data.txt') as file:
        data = [i for i in file.read().strip().split("\n")]

    print(f'Day 23, Part 1--Register a has value {run(data, 1)}')
    # print(f'Day 23, Part 2--Register a has value {run(data, 2)}')


if __name__ == '__main__':
    main()

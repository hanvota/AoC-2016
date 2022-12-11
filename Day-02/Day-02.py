# Advent of Code 2016, Day-02
# https://adventofcode.com/2016
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

moves = 'UDLR'
transition_part_1 = {
    '1': '1412',
    '2': '2513',
    '3': '3623',
    '4': '1745',
    '5': '2846',
    '6': '3956',
    '7': '4778',
    '8': '5879',
    '9': '6989'
}
transition_part_2 = {
    '1': '1311',
    '2': '2623',
    '3': '1724',
    '4': '4834',
    '5': '5556',
    '6': '2A57',
    '7': '3B68',
    '8': '4C79',
    '9': '9989',
    'A': '6AAB',
    'B': '7DAC',
    'C': '8CBC',
    'D': 'BDDD'

}


def next_button(button, direction, table):
    where = moves.find(direction)
    # button = transition_part_1[button][dir]
    # print(move, direction, button)
    return table[button][where]


def decode(input, button, table):
    for input_line in input:
        instruction = input_line.strip()
        # print(f'{instruction}')
        for move in instruction:
            button = next_button(button, move, table)
        print(button, end='')

    print()


if __name__ == '__main__':
    with open('Day-02-data.txt', 'r') as f:
        input_data = f.readlines()

    button = '5'
    print(f'Day 02, Part 1--bathroom code is ', end='')
    decode(input_data, button, transition_part_1)

    button = '5'
    print(f'Day 02, Part 2--bathroom code is ', end='')
    decode(input_data, button, transition_part_2)

    # print(f'Day 02, Part 1--')
    # print(f'Day 02, Part 2--')

# Advent of Code 2016, Day-08
# https://adventofcode.com/2016
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

SCREEN_X = 50  # width
SCREEN_Y = 6  # Height


def initialize(screen, x, y):
    for i in range(y):
        row = list('.' * x)
        screen.append(row)
    return screen


def print_screen(screen):
    for y in range(len(screen)):
        print(''.join(screen[y]))


def do_rect(screen, box):
    dim_x, dim_y = box.split('x')
    # print(dim_x, dim_y)
    for y in range(int(dim_y)):
        for x in range(int(dim_x)):
            screen[y][x] = '#'
    return screen


def shift_row(screen, y, amount):
    # print(y, amount)
    row = ''.join(screen[y])
    for x in range(amount):
        last_char = row[-1]
        row = last_char + row[:-1]  # take the last char and put it at the front
    screen[y] = list(row)
    return screen


def shift_column(screen, x, amount):
    # print(x, amount)
    row = ''
    for y in range(len(screen)):  # convert column x into a string
        row += screen[y][x]
    for y in range(amount):
        last_char = row[-1]
        row = last_char + row[:-1]  # take the last char and put it at the front
    for y in range(len(screen)):  # return the char in the string back to the column
        screen[y][x] = row[y]

    return screen


def do_rotate(screen, axis, amount):
    if axis[0] == 'y':
        screen = shift_row(screen, int(axis[2:]), int(amount))
    else:
        screen = shift_column(screen, int(axis[2:]), int(amount))

    return screen


def pixels_lit(screen):
    size_y = len(screen)
    size_x = len(screen[0])
    count = 0
    for y in range(size_y):
        for x in range(size_x):
            if screen[y][x] == '#':
                count += 1
    return count


def part_1(input_data):
    screen = []
    screen = initialize(screen, SCREEN_X, SCREEN_Y)
    # print_screen(screen)
    for input_line in input_data:
        # print(f'{input_line}')
        line = input_line.strip().split(' ')
        # print(line)
        if line[0] == 'rect':
            screen = do_rect(screen, line[1])
        elif line[0] == 'rotate':
            screen = do_rotate(screen, line[2], line[4])
        else:
            print(f'ERROR--unknown command {line}')
        # print_screen(screen)
    print_screen(screen)
    return pixels_lit(screen)


if __name__ == '__main__':
    with open('Day-08-data.txt', 'r') as f:
        input_data = f.readlines()

    pixel_lit = part_1(input_data)
    print(f'Day 08, Part 1--{pixel_lit} pixels should be lit')
    # the display shown displays the code
    print(f'Day 08, Part 2--Code on screen is "CFLELOYFCS"')

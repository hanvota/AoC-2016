# Advent of Code 2016, Day-xx
# https://adventofcode.com/2016
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.

from collections import deque

PUZZLE_INPUT = 1358
START = [1, 1]
END = [31, 39]
MAZE_SIZE = 10
move = {  # 'direction': (delta_x, delta_y)
    'n': (0, -1),
    'e': (1, 0),
    's': (0, 1),
    'w': (-1, 0)
}


def is_wall(x, y):
    if x < 0 or y < 0:
        return 1
    value = (x * x) + (3 * x) + (2 * x * y) + y + (y * y) + PUZZLE_INPUT
    one_bits = bin(value).count('1')
    return one_bits % 2 == 1


def draw_maze(me, crumb):
    from_y = max(me[1] - 5, 0)
    from_x = max(me[0] - 5, 0)
    for y in range(from_y, from_y + MAZE_SIZE):
        # print('#', end='')
        for x in range(from_x, from_x + MAZE_SIZE):
            if (x, y) in crumb:
                print('.', end='')
            elif [x, y] == me:
                print('@', end='')
            elif is_wall(x, y) == 1:
                print('#', end='')
            else:
                print(' ', end='')
        print()
    # print('#' * (MAZE_SIZE + 2))


def show_valid_move(me, crumb):
    valid = []
    for step in 'nesw':
        next_x = me[0] + move[step][0]
        next_y = me[1] + move[step][1]
        if is_wall(next_x, next_y) or (next_x, next_y) in crumb:
            continue
        valid.append((next_x, next_y))
    # print(f'from {me}, valid-{valid}')
    return valid


def part_1():
    paths = deque()
    me = START
    crumb = [(0, 0), (0, 1)]
    print(crumb)
    # path = 'seesseseenes'
    draw_maze(me, crumb)
    # for step in path:
    valid = show_valid_move(me, crumb)
    paths.extendleft(valid)
    # for v in valid:
    #     paths.appendleft(v)
    steps = 1
    while True:
        crumb.append(tuple(me))
        next_step = paths.popleft()
        me = list(next_step)
        steps += 1
        if me == END:
            print(f'You have arrived at {me}')
            break
        valid = show_valid_move(me, crumb)
        paths.extendleft(valid)

        # for v in valid:
        #     paths.appendleft(v)
        print(f'from {me}, valid-{valid}')

        draw_maze(me, crumb)
    draw_maze(me, crumb)
    return steps


def main():
    print(f'Day xx, Part 1--Number of steps {part_1()}')
    # print(f'Day xx, Part 2--')


if __name__ == '__main__':
    main()

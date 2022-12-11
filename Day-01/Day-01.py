# Advent of Code 2015, Day-01
# https://adventofcode.com/2015
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
"""
               0
               N
               |
    270 W <---   ---> E 90
               |
               S
              180

"""


def turn(heading, direction):
    if direction == 'R':
        heading = (heading + 90) % 360
    else:
        heading = (heading + 360 - 90) % 360
    return heading


def move_part_1(x_, y_, heading, distance_):
    if heading == 0:
        y_ += distance_
    elif heading == 90:
        x_ += distance_
    elif heading == 180:
        y_ -= distance_
    elif heading == 270:
        x_ -= distance_
    else:
        print(f'ERROR--strange heading {heading}')
    return x_, y_


def move_part_2(x_, y_, heading, distance_):
    global trail

    if heading == 0:
        for i in range(1, distance_ + 1):
            new_spot = (x_, y_ + i)
            if new_spot not in trail:
                trail.update([new_spot])
            else:
                break
    elif heading == 90:
        for i in range(1, distance_ + 1):
            new_spot = (x_ + i, y_)
            if new_spot not in trail:
                trail.update([new_spot])
            else:
                break
    elif heading == 180:
        for i in range(1, distance_ + 1):
            new_spot = (x_, y_ - i)
            if new_spot not in trail:
                trail.update([new_spot])
            else:
                break
    elif heading == 270:
        for i in range(1, distance_ + 1):
            new_spot = (x_ - i, y_)
            if new_spot not in trail:
                trail.update([new_spot])
            else:
                break
    else:
        print(f'ERROR--strange heading {heading}')

    return new_spot


if __name__ == '__main__':

    with open('Day-01-data.txt', 'r') as f:
        input_data = f.readlines()
    input_line = input_data[0]

    instruction = input_line.strip().split(', ')
    # print(instruction)
    # instruction = ['R5', 'L5', 'R5', 'R3']  # test data
    cur_heading = 0  # start facing N, x = 0, y = 0
    x = 0
    y = 0

    for i in instruction:
        turn_direction = i[0]
        distance = i[1:]
        # print(f'{turn_direction} for {distance} units')
        cur_heading = turn(cur_heading, turn_direction)
        x, y = move_part_1(x, y, cur_heading, int(distance))

    print(f'Day 01, Part 1--Now at {x}, {y} at {abs(x) + abs(y)} block from starting point and heading {cur_heading}')

    # instruction = ['R9', 'R5', 'R4', 'R3', 'R3', 'R8']  # test data
    # print(instruction)
    cur_heading = 0  # start facing N, x = 0, y = 0
    x = 0
    y = 0
    trail = {(0, 0), }  # initial location. Leaving bread crumbs of spots already passed thru

    j = 0
    for i in instruction:
        turn_direction = i[0]
        distance = i[1:]
        # print(f'{turn_direction} for {distance} units')
        cur_heading = turn(cur_heading, turn_direction)
        x, y = move_part_2(x, y, cur_heading, int(distance))
        j += 1

    # print(j, len(trail), trail)
    print(f'Day 01, Part 2--Now at {x}, {y} at {abs(x) + abs(y)} block from starting point and heading {cur_heading}')
# part 2 = 113 -97.0 -16.0

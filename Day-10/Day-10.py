# Advent of Code 2016, Day-10
# https://adventofcode.com/2016
# Press Double ⇧ to search everywhere for classes, files, tool windows, actions, and settings.
import re

GOAL = (17, 61)
# GOAL = (2, 5)           # goal for the test data

pattern_1 = r'^value (\d+) goes to (.*)$'
pattern_2 = r'^(.+) gives low to (.+) and high to (.+)$'

robots = {  # dictionary of the known robots and what each is holding.
    # 'bot 88': [chip 1, chip 2],
    # 'bot 70': [chip 1, chip 2]
}
# outputs = {  # dictionary of the outputs.
#     # 'output 10': 'value 4',
#     # 'output 12': 'value 8'
# }
instructions = [
    # ['bot 2 gives low to bot 1 and high to bot 0']
    # ['bot 0 gives low to output 2 and high to output 0']
]  # queue of instructions that are pending.


def place(chip, destination):  # place the chip into the destination (a robot or an output), check to see if robot is holding the 2 chips in the goal
    found = None
    if destination not in robots.keys():
        robots[destination] = [chip]
    else:
        robots[destination].append(chip)
        if len(robots[destination]) == 2:
            found = check_goal(destination)
    return found


def check_goal(robot):
    if robot not in robots:
        return None

    robot_content = robots[robot]
    if GOAL[0] in robot_content and GOAL[1] in robot_content:
        return robot
    else:
        return None


def handle_instructions_queue():
    done = False
    while not done:
        done = True  # assume that we are done after this pass thru the queue

        for instruction in instructions:
            giver = instruction[0]  # check the robot at the front of the queue
            # if giver not in robots.keys():
            if giver not in robots:
                continue

            if len(robots[giver]) == 2:  # robot has 2 chips and can perform the instruction
                done = False  # if we have any transaction, we have to go thru the queue again after the pass
                chips = robots[giver]
                low_chip = min(chips[0], chips[1])
                high_chip = max(chips[0], chips[1])
                dest_low = instruction[1]
                dest_high = instruction[2]
                found = place(low_chip, dest_low)
                if found:
                    return found
                found = place(high_chip, dest_high)
                if found:
                    return found
                del robots[giver]
                instructions.remove(instruction)
                break

    return None


def part_1(input_data):
    found = None
    for input_line in input_data:
        if 'goes' in input_line:  # handle command with 'goes' -- 'value 5 goes to bot 2'
            m = re.search(pattern_1, input_line)
            found = place(int(m[1]), m[2])
            if found:
                return found
        else:  # handle command with 'gives' -- 'bot 2 gives low to bot 1 and high to bot 0'
            m = re.search(pattern_2, input_line)
            instructions.append([m[1], m[2], m[3]])

        found = handle_instructions_queue()
        if found:
            return found
    return found


def part_2(input_data):
    for input_line in input_data:
        if 'goes' in input_line:  # handle command with 'goes' -- 'value 5 goes to bot 2'
            m = re.search(pattern_1, input_line)
            _ = place(int(m[1]), m[2])
        else:  # handle command with 'gives' -- 'bot 2 gives low to bot 1 and high to bot 0'
            m = re.search(pattern_2, input_line)
            instructions.append([m[1], m[2], m[3]])

        _ = handle_instructions_queue()
    product = int(robots['output 0'][0]) * int(robots['output 1'][0]) * int(robots['output 2'][0])
    return product


if __name__ == '__main__':
    with open('Day-10-data.txt', 'r') as f:
        input_data = f.readlines()

    print(f'Day 10, Part 1--Robot {part_1(input_data)} is responsible for comparing chips "{GOAL}"')
    print(f'Day 10, Part 2--Product from output 0, output 1 and output 3 is {part_2(input_data)}')

# aoc2016_7a.py
input_file_object = open("Day-07-data.txt")
input_as_string = input_file_object.read()
input_file_object.close()


def noDupes(some_list):
    temp = []
    for x in some_list:
        if x not in temp:
            temp.append(x)
    return temp


input_separated = input_as_string.split('\n')

for i in range(len(input_separated)):
    input_separated[i] = input_separated[i].replace('[', ']')
    input_separated[i] = input_separated[i].split(']')

# input_separated[i][1] will be the hypernet sequence

hypernet_valid = []
hypernet_invalid = []
complete_valid = []

for i in range(len(input_separated)):
    # This for loop goes through the list of instructions
    for j in range(1, len(input_separated[i]), 2):
        # This for loop goes through the hypernet instructions
        for k in range((len(input_separated[i][j]) - 3)):
            # This for loop goes through the actual characters in the HNI
            if input_separated[i][j][k] == input_separated[i][j][k + 3] and input_separated[i][j][k + 1] == input_separated[i][j][k + 2] and input_separated[i][j][k] != input_separated[i][j][k + 1]:
                # If it finds an ABBA sequence
                hypernet_invalid.append(input_separated[i])
                break
        else:
            hypernet_valid.append(input_separated[i])

hypernet_valid = noDupes(hypernet_valid)
hypernet_invalid = noDupes(hypernet_invalid)

for i in range(len(hypernet_invalid)):
    if hypernet_invalid[i] in hypernet_valid:
        hypernet_valid.remove(hypernet_invalid[i])

for i in range(len(hypernet_valid)):
    # This for loop goes through options with a valid hypernet sequences
    for j in range(0, len(hypernet_valid[i]), 2):
        # This for loop goes through the non-hypernet sequences in each line
        for k in range((len(hypernet_valid[i][j]) - 3)):
            # This for loop goes through the actual characters
            if hypernet_valid[i][j][k] == hypernet_valid[i][j][k + 3] and hypernet_valid[i][j][k + 1] == hypernet_valid[i][j][k + 2] and hypernet_valid[i][j][k] != hypernet_valid[i][j][k + 1]:
                # ABBA Sequence found
                complete_valid.append(hypernet_valid[i])
                continue

complete_valid = noDupes(complete_valid)
print(len(complete_valid))
print("Searching for Super Secret Listening")

ssl_valid = []
counter = 0

for i in range(len(input_separated)):
    #
    for j in range(0, len(input_separated[i]), 2):
        # only searches supernet
        for k in range((len(input_separated[i][j]) - 2)):
            if input_separated[i][j][k] == input_separated[i][j][k + 2] and input_separated[i][j][k] != input_separated[i][j][k + 1]:
                # ABA sequence found
                temp = []
                temp = input_separated[i][j][k:k + 3]
                aba = ''.join(temp)
                temp = []
                temp = [aba[1], aba[0], aba[1]]
                bab = ''.join(temp)
                for m in range(1, len(input_separated[i]), 2):
                    #
                    if bab in input_separated[i][m]:
                        ssl_valid.append(input_separated[i])
                        counter += 1
                        continue

ssl_valid = noDupes(ssl_valid)

print(len(ssl_valid))

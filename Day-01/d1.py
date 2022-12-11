if __name__ == '__main__':

    with open('Day-01-data.txt', 'r') as f:
        input_data = f.readlines()
    inp = input_data[0]

PART2 = True
# inp = "R8, R4, R4, R8"  # paste your input here
inp2 = [(s[0], int(s[1:])) for s in inp.split(", ")]
dirs = [0+1j, 1+0j, 0-1j, -1+0j]
cur_dir = 0
cur_pos = 0+0j
seen = {cur_pos}
i=0
for direction, num in inp2:
    cur_dir = (cur_dir + 2*(direction == "L") - 1) % 4
    for i in range(num):
        cur_pos += dirs[cur_dir]
        if PART2 and cur_pos in seen:
            break
        seen.add(cur_pos)
    else:
        i += 1
        continue
    break


print(i,len(seen),seen)
print(f'{cur_pos.imag} {cur_pos.real}')
print(int(abs(cur_pos.imag) + abs(cur_pos.real)))

# part 2 = 113
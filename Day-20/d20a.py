ranges = []
for line in open('Day-20-data.txt', 'r'):
    ranges.append(tuple(map(int, line.split('-'))))
ranges.sort()

lowest = 0
for l, r in ranges:
    if l > lowest:
        break
    if lowest <= r:
        lowest = r + 1

print(f'Day 20, part 1--lowest IP is {lowest}')

ranges = []
for line in open('Day-20-data.txt', 'r'):
    ranges.append(list(map(int, line.split('-'))))
ranges.sort()

i = 0
while i < len(ranges) - 1:

    if ranges[i][1] >= ranges[i + 1][0] - 1:
        ranges[i][1] = max(ranges[i][1], ranges[i + 1][1])
        ranges.pop(i + 1)
    else:
        i += 1

allowed = 4294967296
for l, r in ranges:
    allowed -= r - l + 1

print(f'Day 20, part 1--allowed number of IPs is {allowed}')

import re


def supernets_and_hypernets(s):
    seqs = re.split(r'\[|\]', s)
    return seqs[::2], seqs[1::2]


def has_abba(s):
    # return any(a != b for a, b in re.findall(r'(.)(.)\2\1', s, overlapped=True))
    return any(a != b for a, b in re.findall(r'(.)(.)\2\1', s))


def part1(s):
    cnt = 0
    for line in s.split('\n'):
        supernets, hypernets = supernets_and_hypernets(line)
        if any(has_abba(x) for x in supernets) and not any(has_abba(x) for x in hypernets):
            cnt += 1
    return cnt


def babs_for_abas(s):
    # return [b+a+b for a, b in re.findall(r'(.)(.)\1', s, overlapped=True) if a != b]
    return [b + a + b for a, b in re.findall(r'(.)(.)\1', s) if a != b]


def part2(s):
    cnt = 0
    for line in s.split('\n'):
        supernets, hypernets = supernets_and_hypernets(line)
        babs = [bab for supernet in supernets
                for bab in babs_for_abas(supernet)]
        if any(bab in hypernet for bab in babs
                for hypernet in hypernets):
            cnt += 1
    return cnt


with open('Day-07-data.txt') as f:
    s = f.read().strip()

print(part1(s))
print(part2(s))

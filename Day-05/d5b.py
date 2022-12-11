# https://github.com/Hwesta/advent-of-code/blob/master/aoc2016/day5.py


from __future__ import print_function
import hashlib

import os

def solve(data):
    secret_key = data
    starts_with = '00000'
    start = 0
    password1 = ''
    password2 = [None] * 8
    print('secret', secret_key)
    digest = hashlib.md5()
    digest.update(secret_key.encode('utf8'))
    while True:
        m = digest.copy()
        m.update(str(start).encode('utf8'))
        if m.hexdigest().startswith(starts_with):
            print('found hex', m.hexdigest())

            # Part 1
            if len(password1) < 8:
                password1 += m.hexdigest()[5]
                print('password1', password1, len(password1))

            # Part 2
            index = int(m.hexdigest()[5], 16)
            value = m.hexdigest()[6]
            print('idx', index, 'val', value)
            if index < 8 and password2[index] is None:
                password2[index] = value
                print('password2', password2)

        if len(password1) == 8 and password2.count(None) == 0:
            break

        start += 1

    print('total hashes', start)
    return password1, ''.join(password2)

if __name__ == '__main__':
    this_dir = os.path.dirname(__file__)
    with open(os.path.join(this_dir, 'Day-05-data.txt')) as f:
        data = f.read().strip()

    password1, password2 = solve(data)
    print('The first password is', password1)
    print('The second password is', password2)
""" Day 4: Passport Processing """

import time
import re

def strip_fields_1(passport):
    keys = set()
    for s in passport.strip().split(' '):
        keys.add(s.split(':')[0])
    return keys

def strip_fields_2(passport):
    valid_eye_colors = ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']
    valid_hair_colors = '[a-f0-9]'
    keys = set()
    for s in passport.strip().split(' '):
        key = s.split(':')[0]
        val = s.split(':')[1]
        if key == 'byr' and (1920 <= int(val) <= 2002):
            keys.add(key)
        if key == 'iyr' and (2010 <= int(val) <= 2020):
            keys.add(key)
        if key == 'eyr' and (2020 <= int(val) <= 2030):
            keys.add(key)
        if key == 'hgt':
            if 'cm' in val and (150 <= int(val.split('c')[0]) <= 193):
                keys.add(key)
            if 'in' in val and (59 <= int(val.split('i')[0]) <= 76):
                keys.add(key)
        if key == 'hcl':
            if val[0] == '#' and len(val[1:]) == 6 and len(re.sub(valid_hair_colors, '', val[1:])) == 0:
                keys.add(key)
        if key == 'ecl' and val in valid_eye_colors:
            keys.add(key)
        if key == 'pid' and len(val) == 9 and val.isdigit():
            keys.add(key)
        if key == 'cid':
            keys.add(key)
    return keys

def main():
    """ fetch input, time and call both parts, and print results"""

    # Read Input
    with open('./in.txt', 'r', encoding='utf-8') as file:
        lines = list(map(str.strip, file.readlines()))
        passports = []
        passport = ""
        count = 0
        for line in lines:
            if not line.strip():
                passports.append(passport)
                passport = ""
            else:
                passport = passport + line.strip() + ' '
        passports.append(passport)

    print('Input:\n')
    for p in passports:
        print(f'{p}\n')

    ## Part 1
    begin = time.time()

    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    keys_per_passport = list(map(strip_fields_1, passports))
    valid_passports = 0
    for keys in keys_per_passport:
        if keys.issuperset(required):
            valid_passports += 1

    time.sleep(1)
    time_taken = time.time() - begin

    # Print results and solution
    print(f'# of valid passports: {valid_passports}')
    print(f'Time took: {time_taken}\n')

    ## Part 2
    begin = time.time()

    required = {'byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid'}
    keys_per_passport = list(map(strip_fields_2, passports))
    valid_passports = 0
    for keys in keys_per_passport:
        if keys.issuperset(required):
            valid_passports += 1

    time.sleep(1)
    time_taken = time.time() - begin

    # Print results and solution
    print(f'# of valid passports: {valid_passports}')
    print(f'Time took: {time_taken}\n')


if __name__ == "__main__":
    main()


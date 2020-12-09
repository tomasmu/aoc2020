#input
import os
file = os.path.basename(__file__).replace('.py', '_input.txt')
input = open(file).read()

#format
array = input.split('\n\n')

#puzzle 1
passports = [" ".join(line.splitlines()).split() for line in array]

def has_required_fields(passport):
    required = ["byr", "iyr", "eyr", "hgt", "hcl", "ecl", "pid"] #"cid"
    return all(map(lambda req: req in " ".join(passport), required))

answer1 = sum(map(has_required_fields, passports))
print (answer1)

#puzzle 2
import re
def is_valid_height(height):
    match = re.search(r"^(?P<value>\d{2,3})(?P<unit>cm|in)$", height)
    if not match:
        return False
    value, unit = int(match.group("value")), match.group("unit")
    if unit == 'cm':
        return value >= 150 and value <= 193
    if unit == 'in':
        return value >= 59 and value <= 76
    return False

def is_valid_passport(passport):
    if not has_required_fields(passport):
        return False
    pass_dict = dict(map(lambda x: x.split(":"), passport))
    requirements = [
        1920 <= int(pass_dict['byr']) <= 2002,
        2010 <= int(pass_dict['iyr']) <= 2020,
        2020 <= int(pass_dict['eyr']) <= 2030,
        is_valid_height(pass_dict['hgt']),
        bool(re.search("^#[0-9a-f]{6}$", pass_dict['hcl'])),
        bool(re.search("^(amb|blu|brn|gry|grn|hzl|oth)$", pass_dict['ecl'])),
        bool(re.search("^[0-9]{9}$", pass_dict['pid'])),
    ]
    return all(requirements)

answer2 = sum(map(is_valid_passport, passports))
print(answer2)

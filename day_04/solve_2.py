import re

# create a passports list with all the unverified passports
# this just gets the text into a list form, need to verify fields
def parse_passports():
    passports = []

    with open('input') as input:
        passport = []
        for l in input:
            line = l.strip()
            passport.append(line)

            # this is a blank line, then the previous lines are part of a single passport
            if line == "":
                passports.append(" ".join(passport))
                passport = []
    return passports


def parse_passport(passport):
    fields = {}
    for f in passport.strip().split(" "):
        kv = f.split(":")
        fields[kv[0]] = kv[1]
    
    return fields

def verify_passport_fields(p):
    # cid is an optional field...
    required_fields =['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    
    passport = parse_passport(p)

    # I love set operations
    missing_fields = set(required_fields) - set(passport.keys())

    if len(missing_fields) > 0:
        return False
    else:
        return True

def verify_passport(p):
    # make sure we have all the fields we expect
    if not verify_passport_fields(p):
        return False

    valid = True
    passport = parse_passport(p)

    if int(passport['byr']) < 1920 or int(passport['byr']) > 2002:
        valid = False
    
    if int(passport['iyr']) < 2010 or int(passport['iyr']) > 2020:
        valid = False
    
    if int(passport['eyr']) < 2020 or int(passport['eyr']) > 2030:
        valid = False
    
    if passport['hgt'][-2:] != 'cm' and passport['hgt'][-2:] != 'in':
        valid = False
    
    if passport['hgt'][-2:] == 'cm' and (int(passport['hgt'][0:-2]) < 150 or int(passport['hgt'][0:-2]) > 193):
        valid = False
    
    if passport['hgt'][-2:] == 'in' and (int(passport['hgt'][0:-2]) < 59 or int(passport['hgt'][0:-2]) > 76):
        valid = False
    
    matches = re.findall("[0-9a-z]", passport['hcl'][1:])
    if passport['hcl'][0] != '#' or len(matches) != 6 or len(passport['hcl']) != 7:
        valid = False
    
    if passport['ecl'] not in ['amb', 'blu', 'brn', 'gry', 'grn', 'hzl', 'oth']:
        valid = False
    
    if len(passport['pid']) != 9 or not passport['pid'].isdigit():
        valid = False
    
    return valid

valid = 0
passports = parse_passports()
for p in passports:
    if verify_passport(p):
        valid += 1
        passport = parse_passport(p)

print("Number of valid passports %d out of %d passports" % (valid, len(passports)))
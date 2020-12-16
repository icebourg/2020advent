## This would one be great for Perl's text parsing

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

def verify_passport(p):
    # cid is an optional field...
    required_fields =['byr', 'iyr', 'eyr', 'hgt', 'hcl', 'ecl', 'pid']
    
    passport = parse_passport(p)

    # I love set operations
    missing_fields = set(required_fields) - set(passport.keys())

    if len(missing_fields) > 0:
        return False
    else:
        return True

valid = 0
passports = parse_passports()
for p in passports:
    if verify_passport(p):
        valid += 1
        passport = parse_passport(p)

print("Number of valid passports %d out of %d passports" % (valid, len(passports)))
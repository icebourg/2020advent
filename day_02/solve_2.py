##
# Each line gives the password policy and then the password.
# Each policy actually describes two positions in the password,
# where 1 means the first character, 2 means the second character, and so on. 
# (Be careful; Toboggan Corporate Policies have no concept of "index zero"!) 
# Exactly one of these positions must contain the given letter. Other 
# occurrences of the letter are irrelevant for the purposes of policy enforcement.
#
# How many passwords are valid according to their policies?
## 

def validate_password(low, high, char, password):

    # Both positions can't have it, so special casing it a bit up here
    if password[low] == char and password[high] == char:
        return False
    elif password[low] == char or password[high] == char:
        return True
    else:
        return False

def parse_passwords():
    count = 0
    input = open("input", "r")
    for l in input:
        # parse "$low-$high $char: $password" into variables
        x = l.split(":")
        y = x[0].split(" ")
        z = y[0].split("-")

        low = int(z[0])
        high = int(z[1])
        char = y[1]
        password = x[1]

        if validate_password(low, high, char, password):
            count += 1
    input.close()

    return count

count = parse_passwords()
print("There are %d valid passwords in the input" % count)
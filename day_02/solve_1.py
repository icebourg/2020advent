##
# Each line gives the password policy and then the password.
# The password policy indicates the lowest and highest number
# of times a given letter must appear for the password to be valid.
# For example, 1-3 a means that the password must contain a at least
# 1 time and at most 3 times.
#
# How many passwords are valid according to their policies?
## 

def validate_password(low, high, char, password):
    count = password.count(char)

    if count >= low and count <= high:
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
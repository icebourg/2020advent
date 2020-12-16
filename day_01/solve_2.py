##
## Ok, same problem as before but THREE numbers sum to 2020!
## I could just add more lists and just use more memory to 
## track the problem, but going to try a different approach
## this time that uses more CPU. Will do a recursive search
## to sum up each line with every other line to see which ones
## match up and sum to 2020
##

def recurse(haystack, needles, max_depth):
    if len(needles) < max_depth:
        for i in haystack:
            recurse(haystack, needles + [i], max_depth)

    sum = 0
    # anything times 1 is itself. Thank you math :) 
    total = 1
    for x in needles:
        sum += x
        total *= x
    
    if sum == 2020 and len(needles) == max_depth:
        print ("Found the values! %s; total = %d" % (needles, total) )
        exit

values = []
input = open("input_1", "r")

for l in input:
    values.append(int(l))
input.close()

for i in values:
    recurse(values, [i], 3)

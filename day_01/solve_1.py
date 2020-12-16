##
## Day one! Here we go
## Going to do this in Python.
## My mac has 2.7 which I know is old but trying to keep it relatively stock
##
##
##
## Today's puzzle wants us to find the two values that sum to 2020
## How do?
##
## Here's my approach. For each line, calculate 2020 - l, this will give
## us the value that we're looking for that sums to 2020. Add it to an array.
## Check the array to see if the line we're on matches.
## If it does, great! We found our two values.
## If it doesn't, keep going.
## Means we will need to keep more and more memory on hand as input grows
## 

sums = []
input = open("input_1", "r")

for l in input:
    num = int(l)
    if num in sums:
        opposite = 2020 - num
        print("The two values are %d, %d which sum to %d." % (num, opposite, (num * opposite)))
    sums.append(2020 - num)

input.close()

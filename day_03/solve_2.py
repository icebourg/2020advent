##
## 
##
# Determine the number of trees you would encounter if,
# for each of the following slopes, you start at the
# top-left corner and traverse the map all the way to the bottom:
# 
# Right 1, down 1.
# Right 3, down 1. (This is the slope you already checked.)
# Right 5, down 1.
# Right 7, down 1.
# Right 1, down 2.

# 3936652720 too high

def count_trees(slope, down):
    trees = 0
    position = -1 * slope

    with open('input') as input:
        i = 0
        for l in input:
            i += 1
            position += slope

            if i % down != 0:
                continue

            line = list(l.strip())
            length = len(line)

            if line[position % length] == '#':
                trees = trees + 1
    return trees

total = count_trees(1, 1) * count_trees(3, 1) * count_trees(5, 1) * count_trees(7, 1) * count_trees(1, 2)

print("Sum of all tree slopes is %d" % total)
print("Trees of 1,1 is %d" % count_trees(1, 1))
print("Trees of 3,1 is %d" % count_trees(3, 1))
print("Trees of 5,1 is %d" % count_trees(5, 1))
print("Trees of 7,1 is %d" % count_trees(7, 1))
print("Trees of 1,2 is %d" % count_trees(1, 2))
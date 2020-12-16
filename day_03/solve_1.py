##
## 
##
# Starting at the top-left corner of your map and
# following a slope of right 3 and down 1, how
# many trees would you encounter?

def count_trees(slope):
    trees = 0
    position = -1 * slope

    with open('input') as input:
        for l in input:
            line = list(l.strip())
            length = len(line)
            position += slope

            if line[position % length] == '#':
                trees = trees + 1
    return trees

print("There are %d trees with a slope of 3." % count_trees(3))

def parse_input():
    inputs = []

    with open('input') as input:
        i = []
        for l in input:
            line = l.strip()
            inputs.append(line)
    return inputs

def parse_seat(seat, rows, cols):
    for i in seat[0:7]:
        if i == 'F':
            rows = range(rows[0], rows[int(len(rows) / 2)] + 1)
        else:
            rows = range(rows[int(len(rows) / 2)], rows[-1] + 1)
    
    row = rows[0]

    for i in seat[7:]:
        if i == 'L':
            cols = range(cols[0], cols[int(len(cols) / 2)] + 1)
        else:
            cols = range(cols[int(len(cols) / 2)], cols[-1] + 1)
    
    col = cols[0]

    return row * 8 + col

def common():
    inputs = parse_input()
    seat_ids = []
    for i in inputs:
        seat_ids.append(parse_seat(i, range(0, 128), range(0, 8)))
    
    seat_ids.sort()
    return seat_ids

def part_1():
    seat_ids = common()
    print("The highest seat_id is %d" % (seat_ids[-1]))

def part_2():
    seat_ids = common()
    prev_i = seat_ids[0]
    for i in seat_ids:
        if i - prev_i > 1:
            print("Your seat id is %d" % (i - 1))
            return
        prev_i = i


part_1();
part_2();
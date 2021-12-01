has_increased = 0

with open('input.txt', 'r') as f:
    cur_line = f.readline()
    next_line = f.readline()
    while next_line is not None and next_line != '':
        if int(next_line) > int(cur_line):
            has_increased += 1
        cur_line = next_line
        next_line = f.readline()

print(repr(has_increased))

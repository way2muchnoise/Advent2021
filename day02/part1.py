
def move_sub(h, d, command):
    t, n = command.split(' ')
    n = int(n)
    if t == "forward":
        h += n
    elif t == "down":
        d += n
    elif t == "up":
        d -= n
    return h, d


curr_h = 0
curr_d = 0

with open('input.txt', 'r') as f:
    line = f.readline()
    while line is not None and line != '':
        curr_h, curr_d = move_sub(curr_h, curr_d, line)
        line = f.readline()

print(repr(curr_h * curr_d))


def move_sub(h, d, a, command):
    t, n = command.split(' ')
    n = int(n)
    if t == "forward":
        h += n
        d += a * n
    elif t == "down":
        a += n
    elif t == "up":
        a -= n
    return h, d, a


curr_h = 0
curr_d = 0
curr_a = 0

with open('input.txt', 'r') as f:
    line = f.readline()
    while line is not None and line != '':
        curr_h, curr_d, curr_a = move_sub(curr_h, curr_d, curr_a, line)
        line = f.readline()

print(repr(curr_h * curr_d))

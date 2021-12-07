import re

input_pattern = re.compile(r'(\d+),(\d+) -> (\d+),(\d+)')
grid = [[0 for i in range(1000)] for j in range(1000)]


def draw_line(points):
    global grid
    x1, y1, x2, y2 = points
    x1, y1, x2, y2 = int(x1), int(y1), int(x2), int(y2)
    if x1 == x2:
        for i in range(min(y1, y2), max(y1, y2) + 1):
            grid[x1][i] += 1
    elif y1 == y2:
        for i in range(min(x1, x2), max(x1, x2) + 1):
            grid[i][y1] += 1
    else:  # diagonal 45 degrees
        x_delta = 1 if x1 < x2 else -1
        y_delta = 1 if y1 < y2 else -1
        cur_x, cur_y = x1, y1
        grid[cur_x][cur_y] += 1
        while cur_x != x2:
            cur_x += x_delta
            cur_y += y_delta
            grid[cur_x][cur_y] += 1



with open('input.txt', 'r') as f:
    line = f.readline()
    while line is not None and line != '':
        draw_line(input_pattern.match(line).groups())
        line = f.readline()

dangerous_cells = 0

for row in grid:
    for cell in row:
        if cell >= 2:
            dangerous_cells += 1

print(dangerous_cells)

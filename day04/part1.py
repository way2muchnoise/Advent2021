import re


class Board:
    def __init__(self, lines):
        self.grid = []
        for line in lines:
            self.grid.append(re.split(r'\s+', line.strip()))
        self.marks = [
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False],
            [False, False, False, False, False]
        ]

    def has_bingo_line(self):
        has_bingo = False
        for line in self.marks:
            has_bingo |= line[0] and line[1] and line[2] and line[3] and line[4]
        return has_bingo

    def has_bingo_column(self):
        has_bingo = False
        for i in range(5):
            has_bingo |= self.marks[0][i] and self.marks[1][i] and self.marks[2][i] and self.marks[3][i] and self.marks[4][i]
        return has_bingo

    def has_bingo(self):
        return self.has_bingo_line() or self.has_bingo_column()

    def call_number(self, number):
        for i in range(5):
            for j in range(5):
                if self.grid[i][j] == number:
                    self.marks[i][j] = True

    def get_marked_numbers(self):
        numbers = []
        for i in range(5):
            for j in range(5):
                if self.marks[i][j]:
                    numbers.append(self.grid[i][j])
        return numbers

    def get_unmarked_numbers(self):
        numbers = []
        for i in range(5):
            for j in range(5):
                if not self.marks[i][j]:
                    numbers.append(self.grid[i][j])
        return numbers


boards = []

with open('input.txt', 'r') as f:
    numbers = f.readline()
    f.readline()  # blank line
    line = f.readline()
    while line is not None and line != '':
        boards.append(Board([line, f.readline(), f.readline(), f.readline(), f.readline()]))
        f.readline()  # blank line
        line = f.readline()

numbers = numbers.strip().split(',')
current_number = -1
bingo_board = None

while bingo_board is None:
    current_number += 1
    for board in boards:
        board.call_number(numbers[current_number])
        if board.has_bingo():
            bingo_board = board

sum_unmarked = sum(map(int, bingo_board.get_unmarked_numbers()))

print(sum_unmarked * int(numbers[current_number]))

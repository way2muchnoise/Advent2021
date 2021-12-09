from enum import Enum


class Side(Enum):
    TOP = 'top'
    TOP_LEFT = 'top_left'
    TOP_RIGHT = 'top_right'
    MIDDLE = 'middle'
    BOTTOM_LEFT = 'bottom_left'
    BOTTOM_RIGHT = 'bottom_right'
    BOTTOM = 'bottom'


class Digit(Enum):
    ZERO = [Side.TOP, Side.TOP_LEFT, Side.TOP_RIGHT, Side.BOTTOM_LEFT, Side.BOTTOM_RIGHT, Side.BOTTOM]
    ONE = [Side.TOP_RIGHT, Side.BOTTOM_RIGHT]
    TWO = [Side.TOP, Side.TOP_RIGHT, Side.MIDDLE, Side.BOTTOM_LEFT, Side.BOTTOM]
    THREE = [Side.TOP, Side.TOP_RIGHT, Side.MIDDLE, Side.BOTTOM_RIGHT, Side.BOTTOM]
    FOUR = [Side.TOP_LEFT, Side.TOP_RIGHT, Side.MIDDLE, Side.BOTTOM_RIGHT]
    FIVE = [Side.TOP, Side.TOP_LEFT, Side.MIDDLE, Side.BOTTOM_RIGHT, Side.BOTTOM]
    SIX = [Side.TOP, Side.TOP_LEFT, Side.MIDDLE, Side.BOTTOM_LEFT, Side.BOTTOM_RIGHT, Side.BOTTOM]
    SEVEN = [Side.TOP, Side.TOP_RIGHT, Side.BOTTOM_RIGHT]
    EIGHT = [Side.TOP, Side.TOP_LEFT, Side.TOP_RIGHT, Side.MIDDLE, Side.BOTTOM_LEFT, Side.BOTTOM_RIGHT, Side.BOTTOM]
    NINE = [Side.TOP, Side.TOP_LEFT, Side.TOP_RIGHT, Side.MIDDLE, Side.BOTTOM_RIGHT, Side.BOTTOM]

    @staticmethod
    def by_length(length):
        return list(filter(lambda d: len(d.value) == length, Digit))

    @staticmethod
    def get_value(digit):
        if Digit.ZERO == digit:
            return 0
        elif Digit.ONE == digit:
            return 1
        elif Digit.TWO == digit:
            return 2
        elif Digit.THREE == digit:
            return 3
        elif Digit.FOUR == digit:
            return 4
        elif Digit.FIVE == digit:
            return 5
        elif Digit.SIX == digit:
            return 6
        elif Digit.SEVEN == digit:
            return 7
        elif Digit.EIGHT == digit:
            return 8
        elif Digit.NINE == digit:
            return 9


def analyse_digits(inputs, outputs):
    side_map = {}
    available_letters = list('abcdefg')
    for side in Side:
        side_map[side] = available_letters.copy()
    for letters in inputs:
        digits = Digit.by_length(len(letters))
        if len(digits) == 1:
            for side in Side:
                if side not in digits[0].value:
                    for letter in available_letters:
                        if letter in letters:
                            if letter in side_map[side]:
                                side_map[side].remove(letter)
    has_changed = True
    while has_changed:
        has_changed = False
        solo_letters = []
        for side in Side:
            if len(side_map[side]) == 1:
                solo_letters.append(side_map[side][0])
        for letter in solo_letters:
            for side in Side:
                if len(side_map[side]) > 1 and letter in side_map[side]:
                    side_map[side].remove(letter)
                    has_changed = True
        duo_letters = []
        for side1 in Side:
            if len(side_map[side1]) == 2:
                for side2 in Side:
                    if side1 != side2 and side_map[side1] == side_map[side2]:
                        duo_letters.append((side1, side2, side_map[side2].copy()))
        for duo in duo_letters:
            for side in Side:
                if side != duo[0] and side != duo[1]:
                    for letter in duo[2]:
                        if letter in side_map[side]:
                            side_map[side].remove(letter)
                            has_changed = True
    permutations = [side_map.copy()]
    for side in Side:
        for i in range(len(permutations)):
            current_permutation = permutations.pop(0)
            for letter in side_map[side]:
                new_permutation = current_permutation.copy()
                new_permutation[side] = [letter]
                permutations.append(new_permutation)
    good_permutations = []
    for permutation in permutations:
        if len(set(map(lambda v: v[0], permutation.values()))) == len(available_letters):
            pivoted_permutation = {}
            for digit in Digit:
                letters = ''
                for side in digit.value:
                    letters += permutation[side][0]
                pivoted_permutation[''.join(sorted(letters))] = digit
            good_permutations.append(pivoted_permutation)
    correct_permutation = None
    for permutation in good_permutations:
        correct = True
        for input in inputs:
            correct &= ''.join(sorted(input)) in permutation
        if correct:
            correct_permutation = permutation
    return correct_permutation


total = 0
with open('input.txt', 'r') as f:
    line = f.readline()
    while line is not None and line != '':
        inputs, outputs = line.strip().split(' | ')
        segment_map = analyse_digits(inputs.split(' '), outputs.split(' '))
        digit = ''
        for output in outputs.split(' '):
            digit += repr(Digit.get_value(segment_map[''.join(sorted(output))]))
        total += int(digit)
        line = f.readline()

print(total)

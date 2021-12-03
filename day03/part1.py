bit_dict = {}


def take_bits(bits):
    for i in range(0, len(bits)):
        curr_i = bit_dict.get(i, [0, 0])
        curr_i[int(bits[i])] = curr_i[int(bits[i])] + 1
        bit_dict[i] = curr_i


with open('input.txt', 'r') as f:
    line = f.readline()
    while line is not None and line != '':
        take_bits(line.strip())
        line = f.readline()

gamma = ''
epsilon = ''

for v in bit_dict.values():
    gamma += '1' if v[1] > v[0] else '0'
    epsilon += '0' if v[1] > v[0] else '1'

print(int(gamma, 2) * int(epsilon, 2))

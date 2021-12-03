def take_bits(bit_dict, bits):
    for i in range(0, len(bits)):
        curr_i = bit_dict.get(i, [0, 0])
        curr_i[int(bits[i])] = curr_i[int(bits[i])] + 1
        bit_dict[i] = curr_i


def take_all_bits(all_bits):
    bit_dict = {}
    for bits in all_bits:
        take_bits(bit_dict, bits)
    return bit_dict


def filter_list(to_filter, i, c):
    return list(filter(lambda v: int(v[i]) == c, to_filter))


with open('input.txt', 'r') as f:
    bits_input = list(map(str.strip, f.readlines()))
bit_dict = take_all_bits(bits_input)

gamma_list = bits_input.copy()
epsilon_list = bits_input.copy()

bit_length = len(bits_input[0])

for k in range(0, bit_length):
    if len(gamma_list) > 1:
        v = take_all_bits(gamma_list)[k]
        gamma_list = filter_list(gamma_list, k, 1) if v[1] >= v[0] else filter_list(gamma_list, k, 0)
    if len(epsilon_list) > 1:
        v = take_all_bits(epsilon_list)[k]
        epsilon_list = filter_list(epsilon_list, k, 0) if v[1] >= v[0] else filter_list(epsilon_list, k, 1)


print(int(gamma_list[0], 2) * int(epsilon_list[0], 2))

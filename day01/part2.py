has_increased = 0
window_size = 3
current_position = 1

with open('input.txt', 'r') as f:
    values = list(map(int, f.readlines()))
    while (current_position + window_size) <= len(values):
        window_prev = sum(values[current_position-1:current_position-1+window_size])
        window_curr = sum(values[current_position:current_position+window_size])
        if window_curr > window_prev:
            has_increased += 1
        current_position += 1

print(repr(has_increased))

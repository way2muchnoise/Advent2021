with open('input.txt', 'r') as f:
    line = f.readline()

original_fishes = list(map(int, line.strip().split(',')))
pre_run = 7
mature = pre_run
spawn_pattern = []

while mature > 0:
    to_add = 0
    for i in range(len(original_fishes)):
        original_fishes[i] -= 1
        if original_fishes[i] < 0:
            to_add += 1
            original_fishes[i] = 6
    spawn_pattern.append(to_add)
    mature -= 1

days_to_simulate = 256 - pre_run
rounds = days_to_simulate // pre_run
days_to_simulate = days_to_simulate - rounds * pre_run
total_fish = len(original_fishes) + sum(spawn_pattern)

zero_spawn = [0 for i in range(len(spawn_pattern))]
prev_patterns = [zero_spawn, spawn_pattern.copy()]
while rounds > 0:
    prev_pattern = prev_patterns.pop(0)
    for i in reversed(range(len(spawn_pattern))):
        if i-2 < 0:
            spawn_pattern[i] = spawn_pattern[i] + prev_pattern[i - 2]
        else:
            spawn_pattern[i] = spawn_pattern[i] + spawn_pattern[i - 2]
    rounds -= 1
    prev_patterns.append(spawn_pattern.copy())
    total_fish += sum(spawn_pattern)

prev_pattern = prev_patterns.pop(0)
for i in reversed(range(days_to_simulate)):
    if i-2 < 0:
        spawn_pattern[i] = spawn_pattern[i] + prev_pattern[i - 2]
    else:
        spawn_pattern[i] = spawn_pattern[i] + spawn_pattern[i - 2]

print(total_fish + sum(spawn_pattern[0:days_to_simulate]))

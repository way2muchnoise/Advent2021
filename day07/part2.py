def fuel_cost(start, end):
    return sum(range(abs(end - start)+1))


with open('input.txt', 'r') as f:
    line = f.readline()

positions = list(map(int, line.strip().split(',')))

min_fuel = None

for i in range(min(positions), max(positions) + 1):
    total_fuel_cost = sum(map(lambda p: fuel_cost(p, i), positions))
    if min_fuel is None or total_fuel_cost < min_fuel:
        min_fuel = total_fuel_cost

print(min_fuel)

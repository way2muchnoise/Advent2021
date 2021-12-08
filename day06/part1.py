with open('input.txt', 'r') as f:
    line = f.readline()

fishes = list(map(int, line.strip().split(',')))
days_to_simulate = 80

while days_to_simulate > 0:
    to_add = 0
    for i in range(len(fishes)):
        fishes[i] -= 1
        if fishes[i] < 0:
            to_add += 1
            fishes[i] = 6
    for i in range(to_add):
        fishes.append(8)
    days_to_simulate -= 1
    print(len(fishes))

print(len(fishes))

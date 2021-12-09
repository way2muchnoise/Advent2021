output_counter = 0

with open('input.txt', 'r') as f:
    line = f.readline()
    while line is not None and line != '':
        outputs = line.strip().split(' | ')[1].split(' ')
        for output in outputs:
            l_output = len(output)
            if l_output == 2 or l_output == 3 or l_output == 4 or l_output == 7:
                output_counter += 1
        line = f.readline()

print(output_counter)

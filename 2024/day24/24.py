import time

def get_data(filename='24.in'):
    with open(filename, 'r') as f:
        values, lines = [item.split('\n') for item in f.read().strip().split('\n\n')]
    m = {}
    for i in range(len(values)):
        ref, val = values[i].split(' ')
        m[ref[:-1]] = int(val)
    for i in range(len(lines)):
        lines[i] = lines[i].split(' ')
    return m, lines

def solve(m, lines):
    covered = [False for _ in lines]
    while not all(covered):
        for i, line in enumerate(lines):
            val1, op, val2, _, val3 = line
            if (covered[i] or val1 not in m or val2 not in m):
                continue
            if op == 'XOR':
                m[val3] = m[val1] ^ m[val2]
            elif op == 'OR':
                m[val3] = m[val1] & m[val2]
            else:
                m[val3] = m[val1] | m[val2]
            covered[i] = True
    print(m)

def part_a():
    m, lines = get_data()
    solve(m, lines)

print('-'*64)
t = time.time()
part_a()
print(f'part a completed in {time.time()-t} seconds')
print('-'*64)

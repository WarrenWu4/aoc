import time

with open('25.in', 'r') as f:
    data = f.read().strip().split('\n\n')

def parse_data(data):
    locks, keys = [], []
    for d in data:
        c = '.' if d[0] == '.' else '#'
        d = d.split('\n')[1:-1]
        pins = []
        for col in range(len(d[0])):
            pin_num = 0
            for row in range(len(d)):
                if (d[row][col] == '#'):
                    pin_num += 1
            pins.append(pin_num)
        if (c == '.'):
            keys.append(pins)
        else:
            locks.append(pins)
    return locks, keys

def add_pins(pa, pb):
    p1a, p2a, p3a, p4a, p5a = pa
    p1b, p2b, p3b, p4b, p5b = pb
    return [p1a+p1b, p2a+p2b, p3a+p3b, p4a+p4b, p5a+p5b]

def check_locks(locks, keys):
    total = 0
    for lock in locks:
        for key in keys:
            if (all([v <= 5 for v in add_pins(lock, key)])):
                total += 1
    return total

def part_a(data):
    locks, keys = parse_data(data)
    print(check_locks(locks, keys))

print('-'*64)
t = time.time()
part_a(data)
print(f'part a completed in {time.time()-t} seconds')
print('-'*64)

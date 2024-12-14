import time

filename = 'input.txt'
with open(filename, 'r') as f:
    data = [chunk.split('\n') for chunk in f.read().strip('\n').split('\n\n')]

def get_data(a, b, prize):
    a = [int(n[2:]) for n in a[10:].split(', ')]
    b = [int(n[2:]) for n in b[10:].split(', ')]
    prize = [int(n[2:]) for n in prize[7:].split(', ')]
    return a, b, prize

def part_a(data):
    total = 0
    for a, b, prize in data:
        a, b, prize = get_data(a, b, prize)
        b_press = round((a[1]/a[0] * prize[0] - prize[1])/(a[1]/a[0] * b[0] - b[1]), 2)
        a_press = round((prize[0] - b[0]*b_press)/a[0], 2)
        if (b_press % 1 == 0 and a_press % 1 == 0):
            total += a_press*3 + b_press
    print(int(total))

def part_b(data):
    total = 0
    for a, b, prize in data:
        a, b, prize = get_data(a, b, prize)
        prize = [n+10000000000000 for n in prize]
        b_press = round((a[1]/a[0] * prize[0] - prize[1])/(a[1]/a[0] * b[0] - b[1]), 2)
        a_press = round((prize[0] - b[0]*b_press)/a[0], 2)
        if (b_press % 1 == 0 and a_press % 1 == 0):
            total += a_press*3 + b_press
    print(int(total))

print(f'part a starting...')
start_time = time.time()
part_a(data)
end_time = time.time()
print(f'part a completed in: {end_time-start_time}\n')

print(f'part b starting...')
start_time = time.time()
part_b(data)
end_time = time.time()
print(f'part b completed in: {end_time-start_time}')

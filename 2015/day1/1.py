import time

with open('input.txt', 'r') as f:
    data = list(f.read().strip('\n'))

def part_a(line):
    floor = 0
    for c in line:
        if c == ')':
            floor -= 1
        else:
            floor += 1
    print(floor)

def part_b(line):
    floor = 0
    for i, c in enumerate(line):
        if floor == -1:
            print(i)
            break
        if c == ')':
            floor -= 1
        else:
            floor += 1

start_time = time.time()
part_a(data)
end_time = time.time()
print(f'part a completed in {end_time-start_time}')

start_time = time.time()
part_b(data)
end_time = time.time()
print(f'part b completed in {end_time-start_time}')

import time

with open('input.txt', 'r') as f:
    data = f.read().strip('\n')

def part_a(data):
    visited = set()
    santa_pos = (0, 0)
    delta = {'^': (0, 1), 'v': (0, -1), '<': (-1, 0), '>': (1, 0)}
    for dir in data:
        santa_pos = (santa_pos[0] + delta[dir][0], santa_pos[1] + delta[dir][1])
        visited.add(santa_pos)
    print(len(visited))

def part_b(data):
    visited = set()
    santa_pos = (0, 0)
    robosanta_pos = (0, 0)
    delta = {'^': (0, 1), 'v': (0, -1), '<': (-1, 0), '>': (1, 0)}
    for i, dir in enumerate(data):
        if (i % 2 == 0):
            santa_pos = (santa_pos[0] + delta[dir][0], santa_pos[1] + delta[dir][1])
            visited.add(santa_pos)
        else:
            robosanta_pos = (robosanta_pos[0] + delta[dir][0], robosanta_pos[1] + delta[dir][1])
            visited.add(robosanta_pos)
    print(len(visited))

start_time = time.time()
part_a(data)
end_time = time.time()
print(f'part a completed in {end_time-start_time}')

start_time = time.time()
part_b(data)
end_time = time.time()
print(f'part b completed in {end_time-start_time}')

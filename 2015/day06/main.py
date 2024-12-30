import time

with open('input.txt', 'r') as f:
    data = f.read().strip('\n').split('\n')

def count_lights(lights):
    total = 0
    for i in range(1000):
        for j in range(1000):
            total += lights[i][j]
    print(total)

def part_a(data):
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for instruction in data:
        instruction = instruction.split(' ')
        start = [int(val) for val in instruction[-3].split(',')]
        stop = [int(val) for val in instruction[-1].split(',')]
        for i in range(start[0], stop[0]+1):
            for j in range(start[1], stop[1]+1):
                if (instruction[0] == 'toggle'):
                    lights[i][j] = 1 if lights[i][j]==0 else 0
                else:
                    lights[i][j] = 1 if instruction[1] == 'on' else 0
    count_lights(lights)

def part_b(data):
    lights = [[0 for _ in range(1000)] for _ in range(1000)]
    for instruction in data:
        instruction = instruction.split(' ')
        start = [int(val) for val in instruction[-3].split(',')]
        stop = [int(val) for val in instruction[-1].split(',')]
        for i in range(start[0], stop[0]+1):
            for j in range(start[1], stop[1]+1):
                if (instruction[0] == 'toggle'):
                    lights[i][j] += 2 
                elif (instruction[1] == 'on'):
                    lights[i][j] += 1 
                else:
                    lights[i][j] = max(0, lights[i][j]-1)
    count_lights(lights)


start_time = time.time()
part_a(data)
end_time = time.time()
print(f'part a completed in {end_time-start_time}')

start_time = time.time()
part_b(data)
end_time = time.time()
print(f'part b completed in {end_time-start_time}')

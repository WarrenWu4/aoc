import time

with open('input.txt', 'r') as f:
    data = [l for l in f.read().strip('\n').split('\n')]
    nums = []
    for i in range(len(data)):
        nums.append([int(n) for n in data[i].split('x')])

def part_a(data):
    total = 0
    for [l, w, h] in data:
        sides = [l*w, w*h, h*l]
        total += 2*sum(sides) + min(sides) 
    print(total)

def part_b(data):
    total = 0
    for [l, w, h] in data:
        perimeters = [2*(l+w), 2*(w+h), 2*(h+l)]
        total += (l*w*h) + min(perimeters) 
    print(total)

start_time = time.time()
part_a(nums)
end_time = time.time()
print(f'part a completed in {end_time-start_time}')

start_time = time.time()
part_b(nums)
end_time = time.time()
print(f'part b completed in {end_time-start_time}')

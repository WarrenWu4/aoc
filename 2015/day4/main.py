import time
from hashlib import md5

with open('input.txt', 'r') as f:
    data = f.read().strip('\n')

def part_a(data):
    start = ''
    i = 0
    while (start != '00000'):
        hex_val = md5((data+str(i)).encode()).hexdigest()
        start = hex_val[:5]
        i += 1
    print(i-1)

def part_b(data):
    start = ''
    i = 0
    while (start != '000000'):
        hex_val = md5((data+str(i)).encode()).hexdigest()
        start = hex_val[:6]
        i += 1
    print(i-1)

start_time = time.time()
part_a(data)
end_time = time.time()
print(f'part a completed in {end_time-start_time}')

start_time = time.time()
part_b(data)
end_time = time.time()
print(f'part b completed in {end_time-start_time}')

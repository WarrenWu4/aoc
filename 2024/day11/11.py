import time
from math import floor, log10
from collections import Counter

filename = 'input.txt'
with open(filename, 'r') as f:
    data = [int(x) for x in f.read().strip('\n').split(' ')]
ex_data = [125, 17]

def blink(num):
    if num == 0: 
        return [1]

    digits = floor(log10(num))+1
    if (digits % 2 == 0):
        return [num // 10**(digits//2), num % 10**(digits//2)]
    
    return [num * 2024]

def blink_stones(stones):
    new_stones = Counter()
    for stone, count in stones.items():
        for new_stone in blink(stone):
            new_stones[new_stone] += count
    return new_stones

def a(nums, blinks):
    stones = Counter(nums)
    for _ in range(blinks):
        stones = blink_stones(stones)
    print(sum(stones.values()))
    
start_time = time.time()
a(data, 25)
end_time = time.time()
print(f'part a completed in: {end_time-start_time}')

start_time = time.time()
a(data, 75)
end_time = time.time()
print(f'part b completed in: {end_time-start_time}')

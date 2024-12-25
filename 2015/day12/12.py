import time
import json

with open('12.in', 'r') as f:
    data = f.read().strip()
    str_numbers = [str(n) for n in range(10)]
    str_bounds = ['[', '{', ']', '}']

def part_a():
    curr_nums, res, neg = '', 0, False
    for i, c in enumerate(data):
        if (c in str_numbers):
            if (len(curr_nums) == 0):
                neg = data[i-1] == '-'
            curr_nums += c
        elif (len(curr_nums) != 0):
            res += int(curr_nums) if (not neg) else -int(curr_nums)
            curr_nums = ''
    print(res)

def part_b(obj):
    if type(obj) is int:
        return obj
    if type(obj) is list:
        return sum(map(part_b, obj))
    if type(obj) is dict:
        vals = obj.values()
        if 'red' in vals:
            return 0
        return sum(map(part_b, vals))
    else:
        return 0

print('-'*64)
t = time.time()
part_a()
print(f'part a completed in {time.time()-t} seconds')
print('-'*64)
t = time.time()
print(part_b(json.loads(data)))
print(f'part b completed in {time.time()-t} seconds')
print('-'*64)

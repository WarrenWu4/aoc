from time import time

with open('10.in', 'r') as f:
    data = f.read().strip()

def look_and_say(nums):
    l, new_nums = 0, ''
    for r in range(len(nums)):
        if (nums[l] != nums[r]):
            new_nums += str(r - l) + nums[l]
            l = r
        if (r == len(nums)-1):
            new_nums += str(r - l + 1) + nums[l]
    return new_nums

def sol(nums, iter_nums):
    for _ in range(iter_nums):
        nums = look_and_say(nums)
    print(len(nums))

print('-'*32)
t = time()
sol(data, 40)
print(f'part a completed in {time()-t} seconds')
print('-'*32)
t = time()
sol(data, 50)
print(f'part a completed in {time()-t} seconds')
print('-'*32)

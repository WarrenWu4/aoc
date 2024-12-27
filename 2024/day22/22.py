import time
from collections import defaultdict

with open('22.in', 'r') as f:
    data = [int(i) for i in f.read().strip().split('\n')]

def next_secret(s):
    s_m = s * 64
    s = s ^ s_m % 16777216
    s_m = s // 32
    s = s ^ s_m % 16777216
    s_m = s * 2048
    s = s ^ s_m % 16777216
    return s

def part_a(data):
    banana_map = defaultdict(int)
    for s in data:
        banana_map_sub = {}
        # get all bananas
        bananas = []
        for _ in range(2000):
            bananas.append(s % 10)
            s = next_secret(s)

        # get all changes from bananas
        changes = []
        for i in range(1, len(bananas)):
            changes.append(bananas[i] - bananas[i-1])
        
        # store changes as hash map of k (seq of changes) : v (banans)
        for i in range(0, len(changes)-3):
            change_hash = (changes[i], changes[i+1], changes[i+2], changes[i+3])
            if not change_hash in banana_map_sub:
                banana_map_sub[change_hash] = bananas[i+4]

        # add current hashmap to global hashmap to figure out max val of each seq
        for k, v in banana_map_sub.items():
            banana_map[k] += v

    print(max(banana_map.values()))

print('-'*64)
t = time.time()
part_a(data)
print(f'part a completed in {time.time()-t} seconds')
print('-'*64)

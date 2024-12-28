import time
from collections import defaultdict
from itertools import combinations

with open('23.in', 'r') as f:
    data = f.read().strip().split('\n')

def connect(connection, g):
    n1, n2 = connection.split('-')
    g[n1].append(n2)
    g[n2].append(n1)

def count_t(g):
    total = 0
    doubles = 0
    triples = 0
    for c in g.keys():
        if c[0] != 't':
            continue
        for c1, c2 in combinations(g[c], 2):
            if c1 in g[c2]:
                if c1[0] == 't':
                    if c2[0] == 't':
                        triples += 1
                    else:
                        doubles += 1
                else:
                    if c2[0] == 't':
                        doubles += 1
                total += 1
    return (total - doubles // 2 - 2 * triples // 3)

def part_a(data):
    g = defaultdict(list)
    for line in data:
        connect(line, g)
    print(count_t(g))

print('-'*64)
t = time.time()
part_a(data)
print(f'part a completed in {time.time()-t} seconds')
print('-'*64)

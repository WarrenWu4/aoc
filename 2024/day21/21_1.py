import time
from collections import Counter

with open('a.in', 'r') as f:
    data = f.read().strip().split('\n')
    numpad = {'7': (0, 0), '8': (0, 1), '9': (0, 2), '4': (1, 0), '5': (1, 1), '6': (1, 2), '1': (2, 0), '2': (2, 1), '3': (2, 2), '0': (3, 1), 'A': (3, 2)}
    reverse_numpad = [['7', '8', '9'], ['4', '5', '6'], ['1', '2', '3'], ['x', '0', 'A']]
    dirpad = {'^': (0, 1), 'A': (0, 2), '<': (1, 0), 'v': (1, 1), '>': (1, 2)}
    reverse_dirpad = [['x', '^', 'A'], ['<', 'v', '>']]
    dirpad_m = {'^': (-1, 0), 'v': (1, 0), '<': (0, -1), '>': (0, 1)}

def sub_tuple(start, end):
    return (end[0] - start[0], end[1] - start[1])

def dist_to_dir(dy, dx):
    sx = '<' if dx > 0 else '>'
    sy = '^' if dy > 0 else 'v'
    return sy*abs(dy) + sx*abs(dx) + 'A'
    
def num_to_dir(s):
    start = 'A'
    dir = ''
    for c in s:
        (dy, dx) = sub_tuple(numpad[c], numpad[start])
        dir += dist_to_dir(dy, dx)
        start = c
    return dir

def num_to_num(dir):
    start = 'A'
    num_dir = ''
    for d in dir:
        (dy, dx) = sub_tuple(dirpad[d], dirpad[start])
        num_dir += dist_to_dir(dy, dx)
        start = d
    return num_dir

def decode(dir):
    (x, y) = dirpad['A']
    new_code = ''
    for d in dir:
        if (d == 'A'):
            new_code += reverse_dirpad[x][y]
            continue
        (dx, dy) = dirpad_m[d]
        x += dx
        y += dy 
    return new_code

def decode_to_num(dir):
    (x, y) = numpad['A']
    new_code = ''
    for d in dir:
        if (d == 'A'):
            new_code += reverse_numpad[x][y]
            continue
        (dx, dy) = dirpad_m[d]
        x += dx
        y += dy 
    return new_code

def part_a():
    complexities = 0
    for code in data:
        numeric = int(code[:-1])
        d = num_to_dir(code)
        for _ in range(2):
            d = num_to_num(d)
        print(f'length: {len(d)}, numeric: {numeric}')
        complexities += len(d) * numeric
    print(complexities)

t = time.time()
part_a()
print(f'part a completed in {time.time()-t} seconds')

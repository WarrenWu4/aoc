import time
from functools import cache

with open('19.in', 'r') as f:
    towels, designs = f.read().strip().split('\n\n')
    towels = towels.split(', ')
    designs = designs.split('\n')

@cache
def matches(design):
    if not design:
        return True
    for i in range(1, len(design) + 1):
        prefix = design[0:i]
        suffix = design[i:]
        if prefix in towels and matches(suffix):
            return True
    return False

def part_a(designs):
    total = 0
    for design in designs:
        total += matches(design)
    print(total)

print(f'{'-'*16}')
t = time.time()
part_a(designs)
print(f'part a completed in {time.time()-t} sec\n{'-'*16}')
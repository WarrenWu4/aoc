with open('6_input.txt', 'r') as f:
    data = f.read().strip('\n').split("\n")
    data = [list(d) for d in data]

guard_sprites = {'^': 0, '>': 1, 'v': 2, '<': 3}
directions = [[-1, 0], [0, 1], [1, 0], [0, -1]]
guard = {'x': 0, 'y':0, 'dx': 0, 'dy': 0, 'dir': 0}
num_rows = len(data)
num_cols = len(data[0])
visited = set()

def is_loop(original_guard, map):
    # if new obstacle is visited twice, then it's a loop
    guard = original_guard.copy() 
    loop_visited = set()
    while (0 <= guard['x']+guard['dx'] <= num_rows-1 and 0 <= guard['y']+guard['dy'] <= num_cols-1):
        new_block = map[guard['x']+guard['dx']][guard['y']+guard['dy']]
        if (new_block == '#' or new_block == '0'):
            guard['dir'] = (guard['dir'] + 1) % 4
            guard['dx'] = directions[guard['dir']][0]
            guard['dy'] = directions[guard['dir']][1]
        else:
            guard['x'] += guard['dx']
            guard['y'] += guard['dy']
            if ((guard['x'], guard['y'], guard['dir']) in loop_visited):
                return True
            loop_visited.add((guard['x'], guard['y'], guard['dir']))
    return False

# find position and orientation of guard
for i in range(num_rows):
    for j in range(num_cols):
        if data[i][j] in guard_sprites.keys():
            guard['dir'] = guard_sprites[data[i][j]]
            [guard['dx'], guard['dy']] = directions[guard['dir']]
            guard['x'] = i
            guard['y'] = j

original_guard = guard.copy()
# while guard is within bounds
while (0 <= guard['x']+guard['dx'] <= num_rows-1 and 0 <= guard['y']+guard['dy'] <= num_cols-1):
    new_block = data[guard['x']+guard['dx']][guard['y']+guard['dy']]
    if (new_block == '#'):
        guard['dir'] = (guard['dir'] + 1) % 4
        guard['dx'] = directions[guard['dir']][0]
        guard['dy'] = directions[guard['dir']][1]
    else:
        guard['x'] += guard['dx']
        guard['y'] += guard['dy']
        visited.add((guard['x'], guard['y']))

# simulate all possible obstacle combinations
loops = 0
for coords in visited:
    data[coords[0]][coords[1]] = '0'
    print(f'checking loop for coords: {coords}')
    if (is_loop(original_guard, data)):
        loops += 1
    data[coords[0]][coords[1]] = '.'
print(loops)

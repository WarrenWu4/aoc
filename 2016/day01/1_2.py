with open('1.in', 'r') as f:
    data = f.read().strip().split(', ')

def sol():
    (dx, dy) = (0, -1)
    curr_pos = (0, 0)
    visited = set()
    visited.add(curr_pos)
    for d in data:
        dir, dist = d[0], int(d[1:])
        if (dir == 'R'):
            (dx, dy) = (-dy, dx)
        else:
            (dy, dx) = (-dx, dy) 
        for _ in range(dist):
            curr_pos = (curr_pos[0]+dx, curr_pos[1]+dy)
            if (curr_pos in visited):
                return curr_pos
            visited.add(curr_pos)
    print('uh oh')
    return curr_pos

pos = sol()
print(abs(pos[0]) + abs(pos[1]))

with open('1.in', 'r') as f:
    data = f.read().strip().split(', ')

(dx, dy) = (0, -1)
curr_pos = (0, 0)
for d in data:
    dir, dist = d[0], int(d[1:])
    if (dir == 'R'):
        (dx, dy) = (-dy, dx)
    else:
        (dy, dx) = (-dx, dy) 
    curr_pos = (curr_pos[0]+dx*dist, curr_pos[1]+dy*dist)

print(abs(curr_pos[0]) + abs(curr_pos[1]))

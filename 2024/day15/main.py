import time

with open ('c.in', 'r') as f:
    data = f.read().strip('\n').split('\n\n')
    map = [list(l) for l in data[0].split('\n')]
    moves = "".join(data[1].split('\n'))
directions = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}

def calculate_gps(map):
    gps = 0
    for r in range(len(map)):
        for c in range(len(map[0])):
            if (map[r][c] == 'O'):
                gps += 100 * r + c
    return gps

def move_robot(robot, moves, map):
    for move in moves:
        og_position = (robot[0], robot[1])
        can_move = False
        (dx, dy) = directions[move]
        while (map[robot[0]][robot[1]] != '#'):
            if (map[robot[0]][robot[1]] == '.'):
                can_move = True
                break
            robot = (robot[0] + dy, robot[1] + dx)
        if (not can_move):
            robot = (og_position[0], og_position[1])
        while (can_move):
            if (map[robot[0]][robot[1]] == '.'):
                map[robot[0]][robot[1]] = 'O'
            elif (map[robot[0]][robot[1]] == '@'):
                map[robot[0]][robot[1]] = '.'
                map[robot[0]+dy][robot[1]+dx] = '@'
                og_position = robot = (robot[0]+dy, robot[1]+dx)
                break
            robot = (robot[0] - dy, robot[1] - dx)

def print_map(map):
    for r in range(len(map)):
        for c in range(len(map[0])):
            print(map[r][c], end='')
        print()

def part_a(map, moves):
    robot_pos = (-1, -1)
    for r in range(len(map)):
        for c in range(len(map[0])):
            if (map[r][c] == '@'):
                robot_pos = (r, c)
                break
        if (robot_pos[0] != -1):
            break
    # moves = '<^^>'
    move_robot(robot_pos, moves, map)
    print_map(map)
    ans = calculate_gps(map)
    print(ans)

a_s = time.time()
part_a(map, moves)
a_e = time.time()
print(f'part a completed in {a_e-a_s} seconds')

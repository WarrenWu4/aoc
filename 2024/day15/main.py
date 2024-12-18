import time
import copy

with open ('i.in', 'r') as f:
    data = f.read().strip('\n').split('\n\n')
    map = [list(l) for l in data[0].split('\n')]
    moves = "".join(data[1].split('\n'))
directions = {'^': (0, -1), 'v': (0, 1), '<': (-1, 0), '>': (1, 0)}

def calculate_gps(map):
    gps = 0
    valid_boxes = ['O', '[']
    for r in range(len(map)):
        for c in range(len(map[0])):
            if (map[r][c] in valid_boxes):
                gps += 100 * r + c
    return gps

def print_map(map):
    for r in range(len(map)):
        for c in range(len(map[0])):
            print(map[r][c], end='')
        print()

def get_robot_pos(map):
    for r in range(len(map)):
        for c in range(len(map[0])):
            if (map[r][c] == '@'):
                return (r, c)

def update_map(map):
    new_map = []
    for r in range(len(map)):
        new_map.append([])
        for c in range(len(map[0])):
            block = map[r][c]
            if (block == '#'):
                new_map[r].extend(list('##'))
            elif (block == 'O'):
                new_map[r].extend(list('[]'))
            elif (block == '.'):
                new_map[r].extend(list('..'))
            else:
                new_map[r].extend(list('@.'))
    return new_map

def horizontal_move(pos, move, map):
    # check if can move horizontally
    (dy, dx) = directions[move]
    (x, y) = (pos[0]+dx, pos[1]+dy)
    is_moveable = False
    while (map[x][y] != '#'):
        if (map[x][y] == '.'):
            is_moveable = True
            break
        y += dy
    # if yes then update map and return robot
    if (is_moveable):
        while(map[x][y] != '@'):
            map[x][y] = map[x][y-dy]
            y -= dy
        map[x][y] = '.'
        return (x, y+dy)
    else:
        return pos

def get_boxes(pos, move, map, boxes):
    (dy, dx) = directions[move]
    (x, y) = (pos[0], pos[1])
    if (map[x][y] == '#' or map[x][y] == '.'):
        return
    if (map[x][y] == ']'):
        boxes.append((x,y-1))
        get_boxes((x+dx, y-1+dy), move, map, boxes)
    elif (map[x][y] == '['):
        boxes.append((x,y+1))
        get_boxes((x+dx, y+1+dy), move, map, boxes)
    boxes.append((x,y))
    get_boxes((x+dx, y), move, map, boxes)

def sort_boxes(boxes):
    # sort by x values
    for i in range(len(boxes)):
        for j in range(i+1, len(boxes)):
          if (boxes[j][0] < boxes[i][0]):
            temp = boxes[j]
            boxes[j] = boxes[i]
            boxes[i] = temp
def reverse_sort_boxes(boxes):
    for i in range(len(boxes)):
        for j in range(i+1, len(boxes)):
          if (boxes[j][0] > boxes[i][0]):
            temp = boxes[j]
            boxes[j] = boxes[i]
            boxes[i] = temp

def vertical_move(pos, move, map):
    (dy, dx) = directions[move]
    (x, y) = (pos[0]+dx, pos[1]+dy)
    boxes = [pos]
    get_boxes((x, y), move, map, boxes)
    for (x, y) in boxes:
          if (map[x+dx][y] == '#'):
            return pos
    boxes = list(set(boxes))
    if (dx == 1):
          reverse_sort_boxes(boxes)
    else:
          sort_boxes(boxes)
    for (x, y) in boxes:
        map[x+dx][y] = map[x][y]
        map[x][y] = '.'
    return (x+dx, y)

def part_a(map, moves):
    robot_pos = get_robot_pos(map)
    for move in moves:
        if (move == '<' or move == '>'):
            robot_pos = horizontal_move(robot_pos, move, map)
        else:
            robot_pos = vertical_move(robot_pos, move, map)
    ans = calculate_gps(map)
    print(ans)

def part_b(map, moves):
    map = update_map(map)
    robot_pos = get_robot_pos(map)
    # move_num = 0
    # moves = moves[:23]
    for move in moves:
        if (move == '<' or move == '>'):
            robot_pos = horizontal_move(robot_pos, move, map)
        else:
            robot_pos = vertical_move(robot_pos, move, map)
        """
        move_num += 1
        print(f'Move Number: {move_num}, {move}')
        print_map(map)
        """
    ans = calculate_gps(map)
    print(ans)

a_s = time.time()
part_a(copy.deepcopy(map), moves)
a_e = time.time()
print(f'part a completed in {a_e-a_s} seconds')

b_s = time.time()
part_b(copy.deepcopy(map), moves)
b_e = time.time()
print(f'part b completed in {b_e-b_s} seconds')

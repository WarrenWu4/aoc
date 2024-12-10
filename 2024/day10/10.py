import time

filename = 'input.txt'

with open(filename, 'r') as f:
    data = f.read().strip('\n').split('\n')
    data = [list(v) for v in data]

def climb(map, x, y, visited):
    if (map[x][y] == 9):
        visited.add((x, y))
        return
    # check left
    if (x > 0 and map[x-1][y] == map[x][y]+1):
        climb(map, x-1, y, visited)
    # check right
    if (x < len(map)-1 and map[x+1][y] == map[x][y]+1):
        climb(map, x+1, y, visited)
    # check top
    if (y > 0 and map[x][y-1] == map[x][y]+1):
        climb(map, x, y-1, visited)
    # check bottom
    if (y < len(map[0])-1 and map[x][y+1] == map[x][y]+1):
        climb(map, x, y+1, visited)
        
def climb2(map, x, y, path, paths):
    if (map[x][y] == 9):
        paths.add(path)
        return
    # check left
    if (x > 0 and map[x-1][y] == map[x][y]+1):
        path += (str(x-1)+str(y), )
        climb2(map, x-1, y, path, paths)
    # check right
    if (x < len(map)-1 and map[x+1][y] == map[x][y]+1):
        path += (str(x+1)+str(y), )
        climb2(map, x+1, y, path, paths)
    # check top
    if (y > 0 and map[x][y-1] == map[x][y]+1):
        path += (str(x)+str(y-1), )
        climb2(map, x, y-1, path, paths)
    # check bottom
    if (y < len(map[0])-1 and map[x][y+1] == map[x][y]+1):
        path += (str(x)+str(y+1), )
        climb2(map, x, y+1, path, paths)

def get_starting_pos(data):
    starting_pos = []
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])
            if (data[i][j] == 0):
                starting_pos.append((i, j))
    return starting_pos

def a(data):
    starting_pos = get_starting_pos(data)
    res = 0
    for start in starting_pos:
        visited = set()
        climb(data, start[0], start[1], visited)
        res += len(visited)
    print(res)

def b(data):
    starting_pos = get_starting_pos(data)
    res = 0
    for start in starting_pos:
        paths = set()
        climb2(data, start[0], start[1], (), paths)
        res += len(paths)
    print(res)

start_time = time.time()
a(data)
end_time = time.time()
print(f'part a completed in {end_time-start_time} seconds')

start_time = time.time()
b(data)
end_time = time.time()
print(f'part b completed in {end_time-start_time} seconds')

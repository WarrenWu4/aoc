import time
import heapq

def get_data():
    def str_to_tuple(i):
        i = i.split(',')
        return (int(i[0]), int(i[1]))
    with open('18.in', 'r') as f:
        data = [str_to_tuple(l) for l in f.read().strip('\n').split('\n')]
    return data

def make_map(side, obstacle):
    map = [['.' for _ in range(side)] for _ in range(side)]
    for (x, y) in obstacle:
        map[y][x] = '#'
    return map

def dijkstra(start, end, map):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    pq = [(0, start[0], start[1])]
    distances = {start: 0}
    visited = set()
    while pq:
        dist, x, y = heapq.heappop(pq)
        if (x, y) == end:
            return dist 
        if (x, y) in visited:
            continue
        visited.add((x, y))
        for dir in directions:
            dx, dy = dir
            nx, ny = x + dx, y + dy
            if 0 <= nx < len(map) and 0 <= ny < len(map[0]) and map[nx][ny] != '#':
                if (nx, ny) not in distances or dist+1 < distances[(nx, ny)]:
                    distances[(nx, ny)] = dist+1
                    heapq.heappush(pq, (dist + 1, nx, ny))
    return -1

def part_a(data):
    map = make_map(71, data[:1024])
    start, end = (0, 0), (70, 70)
    print(dijkstra(start, end, map))

def part_b(data):
    map = make_map(71, data[:3000])
    start, end = (0,0), (70, 70)
    for (x, y) in data[3000:3150]:
        map[y][x] = '#'
        if (dijkstra(start, end, map) == -1):
            print(f'{x},{y}')
            break

t = time.time()
part_a(get_data())
print(f'part a completed in {time.time()-t} seconds')

t = time.time()
part_b(get_data())
print(f'part b completed in {time.time()-t} seconds')

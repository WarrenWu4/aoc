import time
import heapq

with open('20.in', 'r') as f:
    map = [list(l) for l in f.read().strip().split('\n')]

def get_start_end(map):
    start = end = None
    for r in range(len(map)):
        for c in range(len(map[0])):
            if (map[r][c] == 'S'):
                start = (r, c)
            elif (map[r][c] == 'E'):
                end = (r, c)
    return start, end

def get_obstacles(map):
    obstacles = []
    directions = [(-1, 0), (1, 0), (0, -1), (0, 1)]
    for r in range(len(map)):
        for c in range(len(map[0])):
            if (map[r][c] == '#'):
                # ignore edges
                if (0 == r or len(map)-1 == r):
                    continue
                if (0 == c or len(map[0])-1 == c):
                    continue
                # ignore walls that are bounded by other walls
                for dr, dc in directions:
                    if (map[r+dr][c+dc] != '#'):
                        obstacles.append((r, c))
                        break
    return obstacles

def dijkstra(start, end, map, comp):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    pq = [(0, start[0], start[1])]
    distances = {start: 0}
    visited = set()
    while pq:
        dist, x, y = heapq.heappop(pq)
        if (x, y) == end:
            return dist 
        if (x, y) in visited or (comp and dist+1 >= 9368-100):
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

def part_a(map):
    start, end = get_start_end(map)
    obstacles = get_obstacles(map)
    original_time = dijkstra(start, end, map, False)
    saved = 0
    iterations = 0
    for (r, c) in obstacles:
        map[r][c] = '.'
        new_time = dijkstra(start, end, map, True)
        if (original_time - new_time >= 100):
            saved += 1
        map[r][c] = '#'
        iterations += 1
        if (iterations % 1000 == 0):
            print(f'at {iterations} iterations and {saved} saves')
    print(saved)

t = time.time()
part_a(map)
print(f'part a completed in {time.time()-t} seconds')

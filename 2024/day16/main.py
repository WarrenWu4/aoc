import time
import heapq
from typing import Tuple

with open('16.in', 'r') as f:
    data = [list(l) for l in f.read().strip('\n').split('\n')]

def get_start_end(map) -> Tuple:
    rows, cols = len(map), len(map[0])
    start = end = None
    for r in range(rows):
        for c in range(cols):
            if (map[r][c] == 'S'):
                start = (r, c)
            elif (map[r][c] == 'E'):
                end = (r, c)
    return (start, end)

def dijkstra(map):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    (start, end) = get_start_end(map)
    pq = [(0, start[0], start[1], 0)]
    visited = {}
    while pq:
        score, x, y, dir = heapq.heappop(pq)
        if (x, y) == end:
            return score
        if (x, y, dir) in visited and visited[(x, y, dir)] <= score:
            continue
        visited[(x, y, dir)] = score
        dx, dy = directions[dir]
        nx, ny = x + dx, y + dy
        if map[nx][ny] != '#':
            heapq.heappush(pq, (score + 1, nx, ny, dir))
        heapq.heappush(pq, (score + 1000, x, y, (dir + 1) % 4))
        heapq.heappush(pq, (score + 1000, x, y, (dir - 1) % 4))
    return -1

def best_path(map):
    directions = [(0, 1), (1, 0), (0, -1), (-1, 0)]
    (start, end) = get_start_end(map)
    pq = [(0, start[0], start[1], 0)]
    visited = {}
    stack = []
    while pq:
        score, x, y, dir = heapq.heappop(pq)
        if (x, y) == end:
            stack.append((x, y, dir))
            visited[(x, y, dir)] = score
            break
        if (x, y, dir) in visited and visited[(x, y, dir)] <= score:
            continue
        visited[(x, y, dir)] = score
        dx, dy = directions[dir]
        nx, ny = x + dx, y + dy
        if map[nx][ny] != '#':
            heapq.heappush(pq, (score + 1, nx, ny, dir))
        heapq.heappush(pq, (score + 1000, x, y, (dir + 1) % 4))
        heapq.heappush(pq, (score + 1000, x, y, (dir - 1) % 4))
    best_path_tiles = set()
    while stack:
        x, y, dir = stack.pop()
        curr_score = visited[(x, y, dir)]
        best_path_tiles.add((x, y))
        for d in range(4):
            dx, dy = directions[d]
            px, py = x - dx, y - dy
            prev_score = curr_score - (1 if (dir == d) else 1001)
            if (px, py, d) in visited and visited[(px, py, d)] == prev_score and map[px][py] != '#':
                stack.append((px, py, d))
    return len(best_path_tiles)

def part_a(map):
    print(dijkstra(map))

def part_b(map):
    print(best_path(map)) 

print(f'{'-'*16}')
t = time.time()
part_a(data)
print(f'part a completed in {time.time()-t} sec\n{'-'*16}')

t = time.time()
part_b(data)
print(f'part b completed in {time.time()-t} sec\n{'-'*16}')

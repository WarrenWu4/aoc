import time
from collections import defaultdict

filename = 'input.txt'
with open(filename, 'r') as f:
    data = f.read().strip('\n').split('\n')

def check_surroundings(row, col, crop, region, data):
    coords = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
    valid_coords = []
    for coord in coords:
        if ((coord[0], coord[1]) in region): continue
        if (0 <= coord[0] < len(data) and 0 <= coord[1] < len(data[0]) and data[coord[0]][coord[1]] == crop):
            valid_coords.append(coord)
    return valid_coords

def get_region(row, col, crop, data):
    region = set({(row, col)})
    coords = check_surroundings(row, col, crop, region, data)
    while len(coords) > 0:
        for i, coord in enumerate(coords):
            region.add((coord[0], coord[1]))
            coords.pop(i)
            coords.extend(check_surroundings(coord[0], coord[1], crop, region, data))
    return region

def calc_perimeter(region):
    perimeter = 0
    for (row, col) in region:
        coords = [(row-1, col), (row+1, col), (row, col-1), (row, col+1)]
        perimeter += 4 - sum([coord in region for coord in coords])
    return perimeter

def calc_sides(region, crop, data):
    sides = set()
    all_corners = set()
    shared_corners = 0
    for (row, col) in region:
        corners = ((row, col), (row, col+1), (row+1, col), (row+1, col+1))
        for corner in corners:
            all_corners.add(corner)
        edges = ((corners[0], corners[1]), (corners[0], corners[2]), (corners[1], corners[3]), (corners[2], corners[3]))
        for edge in edges:
            if edge in sides:
                sides.remove(edge)
            else:
                sides.add(edge)
    for (row, col) in all_corners:
        center = (row, col)
        new_corners = ((row-1, col), (row+1, col), (row, col-1), (row, col+1))
        new_edges = ((center, new_corners[1]), (new_corners[0], center), (new_corners[2], center), (center, new_corners[3]))
        if (new_edges[0] in sides and new_edges[1] in sides):
            if not (0 <= center[0] < len(data) and 0 <= new_corners[0][0] < len(data)):
                continue
            if (0 <= center[1] < len(data[0]) and 0 <= new_corners[0][1] < len(data[0])):
                if (data[center[0]][center[1]] == crop and crop == data[new_corners[0][0]][new_corners[0][1]]):
                    shared_corners += 1
            if (0 <= center[1]-1 < len(data[0]) and 0 <= new_corners[0][1]-1 < len(data[0])):
                if (data[center[0]][center[1]-1] == crop and crop == data[new_corners[0][0]][new_corners[0][1]-1]):
                    shared_corners += 1
        if (new_edges[2] in sides and new_edges[3] in sides):
            if not (0 <= center[1] < len(data[0]) and 0 <= new_corners[2][1] < len(data[0])):
                continue
            if (0 <= center[0] < len(data) and 0 <= new_corners[2][0] < len(data)):
                if (data[center[0]][center[1]] == crop and crop == data[new_corners[2][0]][new_corners[2][1]]):
                    shared_corners += 1
            if (0 <= center[0]-1 < len(data) and 0 <= new_corners[2][0]-1 < len(data)):
                if (data[center[0]-1][center[1]] == crop and crop == data[new_corners[2][0]-1][new_corners[2][1]]):
                    shared_corners += 1
    print(len(sides), shared_corners, len(sides) - shared_corners)
    return (len(sides) - shared_corners)

def part_a(data):
    visited = defaultdict(set)
    ans = 0
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if ((row, col) in visited[char]): continue
            region = get_region(row, col, char, data)
            visited[char].update(region)
            ans += len(region) * calc_perimeter(region)
    print(ans)

def part_b(data):
    visited = defaultdict(set)
    ans = 0
    for row, line in enumerate(data):
        for col, char in enumerate(line):
            if ((row, col) in visited[char]): continue
            region = get_region(row, col, char, data)
            visited[char].update(region)
            ans += len(region) * calc_sides(region, char, data)
    print(ans)
    
"""
print(f'part a starting...')
start_time = time.time()
part_a(data)
end_time = time.time()
print(f'part a completed in: {end_time-start_time}\n')
"""

print(f'part b starting...')
start_time = time.time()
part_b(data)
end_time = time.time()
print(f'part b completed in: {end_time-start_time}')

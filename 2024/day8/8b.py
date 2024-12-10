from collections import defaultdict
import time
start_time = time.time()

with open('8_input.txt', 'r') as f:
    data = f.read().strip('\n').split('\n')
    data = [list(line) for line in data]
    num_rows = len(data)
    num_cols = len(data[0])

# store all coords of nodes with same frequency
node_coords = defaultdict(list)
for x, line in enumerate(data):
    for y, c in enumerate(line):
        if c != '.':
            node_coords[c].append((x, y))

# for each node pair of each unique
# check if antinodes are within bound
antinodes = set()

def get_all_antinodes(v1, v2, node_arr, antinodes):
    antinode1 = (node_arr[y][0]+v2[0], node_arr[y][1]+v2[1])
    antinode2 = (node_arr[x][0]+v1[0], node_arr[x][1]+v1[1])
    while (0 <= antinode1[0] < num_rows and 0 <= antinode1[1] < num_cols):
        antinodes.add(antinode1)
        antinode1 = (antinode1[0]+v2[0], antinode1[1]+v2[1])
    while (0 <= antinode2[0] < num_rows and 0 <= antinode2[1] < num_cols):
        antinodes.add(antinode2)
        antinode2 = (antinode2[0]+v1[0], antinode2[1]+v1[1])

for node in node_coords.keys():
    node_arr = node_coords[node]
    for x in range(len(node_arr)-1):
        for y in range(x+1, len(node_arr)):
            # v1 is vector from x to y and v2 is vector from y to x
            v1 = (node_arr[x][0]-node_arr[y][0], node_arr[x][1]-node_arr[y][1])
            v2 = (v1[0]*-1, v1[1]*-1)
            antinodes.add(node_arr[x])
            antinodes.add(node_arr[y])
            get_all_antinodes(v1, v2, node_arr, antinodes)
print(len(antinodes))

end_time = time.time()
print(f'Completed in {end_time-start_time} s')

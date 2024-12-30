import time
from collections import defaultdict

with open('9in', 'r') as f:
    data = f.read().strip().split('\n')

def parse_data(data):
    new_data = []
    for line in data:
        line = line.split(' ')
        new_data.append((line[0], line[2], int(line[-1])))
    return new_data

def construct_graph(parsed_data):
    graph = defaultdict(lambda: defaultdict(int))
    for v_i, v_f, weight in parsed_data:
        graph[v_i][v_f] = weight
        graph[v_f][v_i] = weight
    return graph

def all_paths(src, graph):
    q = [[src]]
    paths, dist = [], []
    while q:
        nodes = q.pop()
        if (len(nodes) == len(graph.keys())):
            paths.append(nodes)
        for adj in graph[nodes[-1]].keys():
            if adj not in nodes:
                q.append(nodes+[adj])
    for path in paths:
        d = 0
        for i in range(len(path)-1):
            start, stop = path[i], path[i+1]
            d += graph[start][stop]
        dist.append(d)
    return dist

def sol(type):
    d = parse_data(data)
    graph = construct_graph(d)
    path_len = float('inf') if (type == 'min') else 0
    for k in graph.keys():
        if (type == 'min'):
            path_len = min(all_paths(k, graph) + [path_len])
        else:
            path_len = max(all_paths(k, graph) + [path_len])
    print(path_len)

print('-'*32)
t = time.time()
sol('min')
print(f'part a completed in {time.time()-t} seconds')
print('-'*32)
t = time.time()
sol('max')
print(f'part b completed in {time.time()-t} seconds')
print('-'*32)

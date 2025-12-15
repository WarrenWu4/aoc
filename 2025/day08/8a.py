filename = '8_ex_input.txt'
filename = '8_input.txt'

connections = 10 if filename == '8_ex_input.txt' else 1000

with open(filename) as f:
  data = f.read().strip('\n').split('\n')

coords = [tuple(int(num) for num in line.split(',')) for line in data]
distances = []

def dist(a, b):
  x1, y1, z1 = a
  x2, y2, z2 = b
  return ((x2-x1)**2 + (y2-y1)**2 + (z2-z1)**2) ** (1/2)

def product(arr):
  res = 1
  for num in arr:
    res *= num
  return res

for i in range(len(coords)):
  for j in range(i+1, len(coords)): 
    ci, cj = coords[i], coords[j]
    distances.append((dist(ci, cj), i, j))
distances.sort()
assert(len(distances) == (len(coords)*(len(coords)-1) // 2))
# print(distances[:2])

circuits = []
for d, i, j in distances[:connections]:
  found = []
  for k, value in enumerate(circuits):
    if coords[i] in value[1] or coords[j] in value[1]:
      circuits[k][1].add(coords[i])
      circuits[k][1].add(coords[j])
      circuits[k][0] = len(circuits[k][1])
      found.append(k)
  if len(found) == 0:
    circuits.append([2, set({coords[i], coords[j]})])
  elif len(found) != 1:
    start = found.pop(0)
    new_set = circuits[start][1]
    for i in found:
      for value in circuits[i][1]:
        new_set.add(value)
      circuits[i][0] = 0
      circuits[i][1] = {}
    circuits[start][1] = new_set
    circuits[start][0] = len(new_set)
  # print(circuits)

circuits.sort(reverse=True)
# print(circuits)
res = product([val for val, _ in circuits[:3]])
print(res)


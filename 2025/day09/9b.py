from dataclasses import dataclass

@dataclass
class Point:
  x: int
  y: int

@dataclass
class Range:
  min: int
  max: int

filename = '9_ex_input.txt'
filename = '9_input.txt'

with open(filename) as f:
  data = []
  for line in f.read().strip('\n').split('\n'):
    x, y= [int(num) for num in line.split(',')]
    data.append(Point(x, y))
  y_vals = [p.y for p in data]
  x_vals = [p.x for p in data]
  n = len(data)

y_min, y_max = min(y_vals), max(y_vals)
x_max, x_min = max(x_vals), min(x_vals)
y_bounds = [Range(y_max, y_min) for _ in range(x_max-x_min+1)]
x_bounds = [Range(x_max, x_min) for _ in range(y_max-y_min+1)]

p1 = data[0]
for p2 in data[1:]+[data[0]]:
  if (p1.x == p2.x):
    x = p1.x-x_min
    y_bounds[x].min = min(y_bounds[x].min, p1.y, p2.y)
    y_bounds[x].max= max(y_bounds[x].max, p1.y, p2.y)
    start, end = min(p1.y, p2.y)-y_min, max(p1.y, p2.y)-y_min+1
    for y in range(start, end):
      x_bounds[y].min = min(x_bounds[y].min, p1.x)
      x_bounds[y].max = max(x_bounds[y].max, p1.x)
  else:
    y = p1.y-y_min
    x_bounds[y].min = min(x_bounds[y].min, p1.x, p2.x)
    x_bounds[y].max= max(x_bounds[y].max, p1.x, p2.x)
    start, end = min(p1.x, p2.x)-x_min, max(p1.x, p2.x)-x_min+1
    for x in range(start, end):
      y_bounds[x].min = min(y_bounds[x].min, p1.y)
      y_bounds[x].max= max(y_bounds[x].max, p1.y)
  p1 = p2
# print(x_bounds)
# print(y_bounds)

res = 0
for i in range(n):
  for j in range(i+1, n):
    p1, p2 = data[i], data[j]
    if (p1.y == p2.y or p1.x == p2.x):
      res = max(res, abs(p2.x-p1.x), abs(p2.y-p1.y))
      continue
    valid = True 
    corner_points = [
      Point(min(p1.x, p2.x), min(p1.y, p2.y)), # top left
      Point(max(p1.x, p2.x), min(p1.y, p2.y)), # top right
      Point(min(p1.x, p2.x), max(p1.y, p2.y)), # bot left
      Point(max(p1.x, p2.x), max(p1.y, p2.y))  # bot right
    ]

    # FIX: updated to check that the rectangle fully connects
    # thx reddit :))

    # horizontal -> check y_bounds
    for x in range(corner_points[0].x, corner_points[1].x+1):
      if not (y_bounds[x-x_min].min <= corner_points[0].y <= y_bounds[x-x_min].max):
        valid = False
        break
      if not (y_bounds[x-x_min].min <= corner_points[2].y <= y_bounds[x-x_min].max):
        valid = False
        break
    # vertical -> check x_bounds 
    for y in range(corner_points[0].y, corner_points[2].y+1):
      if not (x_bounds[y-y_min].min <= corner_points[0].x <= x_bounds[y-y_min].max):
        valid = False
        break
      if not (x_bounds[y-y_min].min <= corner_points[2].x <= x_bounds[y-y_min].max):
        valid = False
        break

    if not valid:
      continue

    length = corner_points[1].x - corner_points[0].x+1
    width = corner_points[2].y - corner_points[0].y+1
    res = max(res, length * width)
print(res)


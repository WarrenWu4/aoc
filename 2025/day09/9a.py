def calc_square(p1, p2):
  x1, y1 = p1
  x2, y2 = p2
  num_x = abs(x2-x1)+1
  num_y = abs(y2-y1)+1
  return num_x * num_y

assert(calc_square((2,5), (9,7)) == 24)
assert(calc_square((7,1), (11,7)) == 35)

filename = '9_ex_input.txt'
filename = '9_input.txt'

with open(filename) as f:
  data = [tuple(int(num) for num in line.split(',')) for line in f.read().strip('\n').split('\n')]
  n = len(data)

res = 0
for i in range(n):
  for j in range(i+1, n):
    res = max(res, calc_square(data[i], data[j]))
print(res)


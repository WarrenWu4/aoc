filename = '7_ex_input.txt'
filename = '7_input.txt'

with open(filename) as f:
  data = f.read().strip('\n').split('\n')

n, m = len(data), len(data[0])
paths = set() 
res = 0
for r in range(n):
  for c in range(m):
    if data[r][c] == 'S':
      paths.add((r+1, c))
    if data[r][c] == '^':
      for row, col in paths:
        if col == c:
          paths.remove((row, col))
          if 0 < col < m-1:
            res += 1
          if col > 0:
            paths.add((row, col-1))
          if col < m-1:
            paths.add((row, col+1))
          break
  # print(f'After Row: {r} -> Paths: {paths}')
print(res)

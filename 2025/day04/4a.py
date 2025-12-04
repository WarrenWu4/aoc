filename = '4_ex_input.txt'
filename = '4_input.txt'

with open(filename) as f:
  data = f.read().strip('\n').split('\n')

def check_adjacent(r, c):
  dir = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
  total_adjacent = 0
  for dr, dc in dir:
    nr, nc = r+dr, c+dc
    if (0 <= nc < len(data[0]) and 0 <= nr < len(data)):
      total_adjacent += data[nr][nc] == '@'
  return total_adjacent < 4

res = 0
for i in range(len(data)):
  for j in range(len(data[i])):
    if (data[i][j] == '@'):
      res += check_adjacent(i, j)
print(res)

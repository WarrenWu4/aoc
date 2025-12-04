filename = '4_ex_input.txt'
filename = '4_input.txt'

with open(filename) as f:
    data = [list(value) for value in f.read().strip('\n').split('\n')]
n, m = len(data), len(data[0])

papers = set()
for i in range(n):
    for j in range(m):
        if (data[i][j] == '@'):
            papers.add((i, j))

def check_adjacent(r, c):
  dir = [(1, 0), (1, 1), (1, -1), (-1, 0), (-1, 1), (-1, -1), (0, 1), (0, -1)]
  total_adjacent = 0
  for dr, dc in dir:
    nr, nc = r+dr, c+dc
    if (0 <= nc < m and 0 <= nr < n):
      total_adjacent += data[nr][nc] == '@'
  return total_adjacent < 4

res = 0
snapshot_res = -1
while snapshot_res != res:
    snapshot_res = res
    removed = []
    for r, c in papers:
        if (data[r][c] == '@' and check_adjacent(r, c)):
            data[r][c] = '.'
            res += 1
            removed.append((r, c))
    for r, c in removed:
        papers.remove((r, c))
print(res)

"""
might be a math solution
but dfs seems easier since 
it kind of looks like a binary tree

ok recursive implementation might hit max stack
lemme try the iterative way
naw this shit way too slow i gotta figure
out the math trick for it

ANOTHER OBSERVATION: no consecutive splitters in a row

progression for each splitter hit
1 -> 2 -> 4 -> 8 -> 13 -> 20 -> 26 -> 40
----
0 -> 1 -> 2 -> 3 -> 3 -> 4 -> 3 -> 6
2^0, 2^1, 2^2, 2^3, 2^3+2^2+2^1, 2^4+2^2, 2^4+2^2+2^1, 2^5+2^3

2^(hit-1)+prev+strays
1 -> 2 -> 4 -> 8 -> 13 -> 20 -> 26 -> 40

1
2^0 + 1 = 2
2^1 + 2 = 4
2^2 + 4 = 8
2^2 + 8 + 1 = 13
2^3 + 12 = 20 (don't double count same stray)
2^2 + 20 + 2 = 26
2^4 + 24 = 40 (don't double count same stray)

1
2^0 + 1 = 2
2^0 + 2 = 3

how do i count strays?
maybe strays-1? -> figured it out, don't double count strays
can count strays by checking if it hits bottom i.e. there is not any splitters in the path

ok wait that didnt work
i had to look it up but 
its just pascal triangle ;-;
"""

from collections import defaultdict


filename = '7_ex_input.txt'
filename = '7_input.txt'

with open(filename) as f:
  data = f.read().strip('\n').split('\n')

n, m = len(data), len(data[0])
paths = defaultdict(int)
paths[data[0].find('S')] = 1

for r in range(1, n):
  for c in range(m):
    if data[r][c] == '.': continue
    for path_col, path_val in paths.items():
      if path_col == c:
        del paths[path_col]
        if path_col > 0:
          paths[c-1] += path_val
        if path_col < m-1:
          paths[c+1] += path_val
        break

print(sum([val for _, val in paths.items()]))

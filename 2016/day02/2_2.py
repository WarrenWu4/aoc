with open('2.in', 'r') as f:
    d = f.read().strip().split('\n')

keypad = [['', '', '1', '', ''],
          ['', '2', '3', '4', ''],
          ['5', '6', '7', '8', '9'],
          ['', 'A', 'B', 'C', ''],
          ['', '', 'D', '', '']]
dir = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
code = ''

start_pos = (0, 2)
for l in d:
    for c in l:
        (dx, dy) = dir[c]
        (nx, ny) = (start_pos[0]+dx, start_pos[1]+dy)
        if (0 <= nx < 5 and 0 <= ny < 5 and keypad[ny][nx] != ''):
            start_pos = (nx, ny)
    code += keypad[start_pos[1]][start_pos[0]]
print(code)

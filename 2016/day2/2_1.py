with open('2.in', 'r') as f:
    d = f.read().strip().split('\n')

keypad = [[str(i+1) for i in range(j, j+3)] for j in range(0, 9, 3)]
dir = {'U': (0, -1), 'D': (0, 1), 'L': (-1, 0), 'R': (1, 0)}
code = ''

start_pos = (1, 1)
for l in d:
    for c in l:
        (dx, dy) = dir[c]
        if (0 <= start_pos[0]+dx < 3 and 0 <= start_pos[1]+dy < 3):
            start_pos = (start_pos[0]+dx, start_pos[1]+dy)
    code += keypad[start_pos[1]][start_pos[0]]
print(code)

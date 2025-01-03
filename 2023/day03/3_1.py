with open('3.in', 'r') as f:
    d = f.read().strip().split('\n')

bound_x, bound_y = len(d[0]), len(d)
digits = [str(i) for i in range(10)]
total = 0

def scan(i, j):
    for dy in [-1, 0, 1]:
        for dx in [-1, 0, 1]:
            if (0 <= j+dx < bound_x and 0 <= i+dy < bound_y):
                if d[i+dy][j+dx] != '.' and d[i+dy][j+dx] not in digits:
                    return True
    return False

for i, l in enumerate(d):
    part, valid = '', False
    for j, c in enumerate(l):
        if c in digits:
            if scan(i, j):
                valid = True
            part += c
        else:
            if valid:
                total += int(part)
            part, valid = '', False
print(total)

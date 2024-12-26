with open('3.in', 'r') as f:
    d = f.read().strip().split('\n')

def check_valid(sides):
    (s1, s2, s3) = sides
    return (s1+s2 > s3) and (s2+s3 > s1) and (s3+s1 > s2)

total = 0
for i in range(0, len(d), 3):
    # get everything in a 3x3
    sides = [[], [], []]
    counter = 0
    for j in range(3):
        for c in d[i+j].split(' '):
            if (c != ''):
                sides[counter%3].append(int(c))
                counter += 1
    for side in sides:
        if (check_valid(side)):
            total += 1
print(total)
    

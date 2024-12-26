with open('3.in', 'r') as f:
    d = f.read().strip().split('\n')

def check_valid(sides):
    (s1, s2, s3) = sides
    return (s1+s2 > s3) and (s2+s3 > s1) and (s3+s1 > s2)

total = 0
for t in d:
    s = []
    for i in t.split(' '):
        if (i != ''):
            s.append(int(i))
    if (check_valid(s)):
        total += 1
print(total)
    

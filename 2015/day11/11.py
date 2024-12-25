import time

def inc_password(p):
    p, i = list(p), -1
    while p:
        if (p[i] == 'z'):
            p[i] = 'a'
            i -= 1
        else:
            p[i] = chr(ord(p[i])+1)
            return ''.join(p)

def check_password(p):
    counter = {'pairs': 0, 'inc': 0}
    for i in range(1, len(p)-1):
        if (ord(p[i-1])+1 == ord(p[i]) == ord(p[i+1])-1):
            counter['inc'] += 1
    i = 0
    while (i < len(p)-1):
        if (p[i] == p[i+1]):
            counter['pairs'] += 1
            i += 1
        i += 1
    invalid_chars = ['i', 'o', 'l']
    for invalid_char in invalid_chars:
        if invalid_char in p:
            return False
    return counter['pairs'] >= 2 and counter['inc'] >= 1

def solve(p):
    # BRUTE FORCE FOR THE WIN!!
    iter = 0 # hard cap that shit at like 100,000,000
    while (not check_password(p) and iter < 100_000_000):
        p = inc_password(p)
        iter += 1
    print(p, iter)
    p = inc_password(p)
    iter = 0
    while (not check_password(p) and iter < 100_000_000):
        p = inc_password(p)
        iter += 1
    print(p, iter)

password = 'hxbxwxba'

print('-'*32)
t = time.time()
solve(password)
print(f'part a & b completed in {time.time()-t} seconds')
print('-'*32)


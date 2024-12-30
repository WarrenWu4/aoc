import time

with open('8.in', 'r') as f:
    data = f.read().strip().split('\n')

def sol():
    total = 0
    for line in data:
        code_len, str_len = len(line), 2
        for c in line:
            if (c == '"' or c == '\\'):
                str_len += 2
            else:
                str_len += 1
        total += str_len - code_len
    print(total)

t = time.time()
sol()
print(f'part b completed in {time.time()-t} seconds')

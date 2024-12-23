import time

with open('8.in', 'r') as f:
    data = f.read().strip().split('\n')

t = time.time()
total = 0
for line in data:
    code_len, str_len, i = len(line), 0, 0
    line = line[1:-1]
    while (i < len(line)):
        if (i <= len(line)-1 and line[i:i+2] == '\\\\' or line[i:i+2] == '\\"'):
            i += 1
        elif (i <= len(line)-1 and line[i:i+2] == '\\x'):
            i += 3
        i += 1
        str_len += 1
    total += code_len - str_len
print(total)
print(f'part a completed in {time.time()-t} seconds')

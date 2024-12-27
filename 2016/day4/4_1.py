from collections import defaultdict

with open('4.in', 'r') as f:
    d = f.read().strip().split('\n')

def is_real(data, checksum):
    counter = defaultdict(int)
    for char in data:
        counter[char] += 1
    data = list(set(data))
    for i in range(len(data)):
        for j in range(i, len(data)):
            di, dj = counter[data[i]], counter[data[j]]
            ci, cj = ord(data[i]), ord(data[j])
            if (di < dj or di == dj and ci > cj):
                data[i], data[j] = data[j], data[i]
    return ''.join(data[:5]) == checksum

def parse_data(line):
    line = line.split('-')
    info = line[-1].split('[')
    return ''.join(line[:-1]), int(info[0]), info[1][:-1]

res = 0
for l in d:
    data, sector_id, checksum = parse_data(l)
    if is_real(data, checksum):
        res += sector_id
print(res)


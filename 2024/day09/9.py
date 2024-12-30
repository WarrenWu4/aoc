import time

def part_a(data):
    new_data = []
    res = 0
    for i, num in enumerate(data):
        id = i//2 if (i%2==0) else -1
        new_data.extend([id]*int(num))
    ptr = len(new_data)-1
    for i, num in enumerate(new_data):
        if (num == -1):
            while (i < ptr and new_data[ptr] == -1):
                ptr -= 1
            if (i < ptr): 
                new_data[i] = new_data[ptr]
                new_data[ptr] = -1
                ptr -= 1
    for i, num in enumerate(new_data):
        if (num != -1):
            res += i * num
    print(res)

def part_b(data):
    data = [int(v) for v in data] 
    ids = []
    res = 0
    for i in range(len(data)):
        id = i//2 if (i%2==0) else -1
        ids.append(id)
    ptr = 1
    while (ptr < len(data)):
        if (ids[ptr] != -1):
            ptr += 1
            continue
        for i in range(len(data)-1, ptr, -1):
            if (ids[i] == -1 or data[i] > data[ptr]):
                continue
            if (data[i] == data[ptr]):
                ids[ptr] = ids[i]
                ids[i] = -1
                break
            else:
                remaining_blanks = data[ptr]-data[i]
                data[ptr] = data[i]
                ids[ptr] = ids[i]
                ids[i] = -1
                data.insert(ptr+1, remaining_blanks)
                ids.insert(ptr+1, -1)
                break
        ptr += 1
    running_val = 0
    for id, nums in zip(ids, data):
        if (id == -1):
            running_val += nums
            continue
        res += (id * nums * (2 * running_val + (nums-1)) // 2)
        running_val += nums
    print(res)

# filename = 'input_ex.txt'
filename = 'input.txt'
with open(filename, 'r') as f:
    data = list(f.read().strip('\n'))

start_time = time.time()
part_a(data)
end_time = time.time()
print(f'part a completed in: {end_time-start_time}')

start_time = time.time()
part_b(data)
end_time = time.time()
print(f'part b completed in: {end_time-start_time}')

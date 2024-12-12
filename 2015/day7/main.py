import time

with open('input.txt', 'r') as f:
    data = [i.split(' ') for i in f.read().strip('\n').split('\n')]

def part_a(data):
    m = {} 
    for i, instruction in enumerate(data):
        if (len(instruction) == 3 and instruction[0].isnumeric()):
            m[instruction[-1]] = int(instruction[0])
            data.pop(i)
    while len(data) > 0:
        for i, instruction in enumerate(data):
            var = instruction[-1]
            if 'NOT' in instruction:
                if instruction[1] in m.keys():
                    m[var] = (1 << 16) - 1 - m[instruction[1]]
                    data.pop(i)
            else:
                if (len(instruction) == 3 and instruction[0] in m.keys()):
                    m[var] = m[instruction[0]]
                    data.pop(i)
                    continue
                if (len(instruction) == 3):
                    continue

                val1 = int(instruction[0]) if instruction[0].isnumeric() else m[instruction[0]] if instruction[0] in m.keys() else None
                val2 = int(instruction[2]) if instruction[2].isnumeric() else m[instruction[2]] if instruction[2] in m.keys() else None
                if 'AND' in instruction and val1 != None and val2 != None:
                    m[var] = val1 & val2
                    data.pop(i)
                elif 'OR' in instruction and val1 != None and val2 != None:
                    m[var] = val1 ^ val2
                    data.pop(i)
                elif 'LSHIFT' in instruction and val1 != None and val2 != None:
                    m[var] = val1 << val2
                    data.pop(i)
                elif 'RSHIFT' in instruction and val1 != None and val2 != None:
                    m[var] = val1 >> val2
                    data.pop(i)
                else:
                    continue
    print(m['a'])

def part_b(data):
    m = {} 
    for i, instruction in enumerate(data):
        if (len(instruction) == 3 and instruction[0].isnumeric()):
            m[instruction[-1]] = int(instruction[0])
            data.pop(i)
    m['b'] = 46065
    while len(data) > 0:
        for i, instruction in enumerate(data):
            var = instruction[-1]
            if 'NOT' in instruction:
                if instruction[1] in m.keys():
                    m[var] = (1 << 16) - 1 - m[instruction[1]]
                    data.pop(i)
            else:
                if (len(instruction) == 3 and instruction[0] in m.keys()):
                    m[var] = m[instruction[0]]
                    data.pop(i)
                    continue
                if (len(instruction) == 3):
                    continue

                val1 = int(instruction[0]) if instruction[0].isnumeric() else m[instruction[0]] if instruction[0] in m.keys() else None
                val2 = int(instruction[2]) if instruction[2].isnumeric() else m[instruction[2]] if instruction[2] in m.keys() else None
                if 'AND' in instruction and val1 != None and val2 != None:
                    m[var] = val1 & val2
                    data.pop(i)
                elif 'OR' in instruction and val1 != None and val2 != None:
                    m[var] = val1 ^ val2
                    data.pop(i)
                elif 'LSHIFT' in instruction and val1 != None and val2 != None:
                    m[var] = val1 << val2
                    data.pop(i)
                elif 'RSHIFT' in instruction and val1 != None and val2 != None:
                    m[var] = val1 >> val2
                    data.pop(i)
                else:
                    continue
    print(m['a'])

start_time = time.time()
part_a(data.copy())
end_time = time.time()
print(f'part a completed in {end_time-start_time}')

start_time = time.time()
part_b(data)
end_time = time.time()
print(f'part b completed in {end_time-start_time}')

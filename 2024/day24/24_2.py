import time
import re

def get_data(filename='24.in'):
    with open(filename, 'r') as f:
        values, lines = f.read().strip().split('\n\n')
    store, wires = {}, []
    values, lines = values.split('\n'), lines.split('\n')
    for i in range(len(values)):
        ref, val = values[i].split(': ')
        store[ref] = int(val)
    for i in range(len(lines)):
        n1, op, n2, _, n3 = lines[i].split(' ')
        wires.append([n1, op, n2, n3])
    return store, wires

def perform_op(n1, op, n2, n3, store):
    assert(op == 'XOR' or op == 'OR' or op == 'AND')
    if op == 'XOR':
        store[n3] = store[n1] ^ store[n2]
    elif op == 'OR':
        store[n3] = store[n1] | store[n2]
    else:
        store[n3] = store[n1] & store[n2]

def isolate_store(store):
    pattern = r"^z\d+$"
    new_store = {}
    for k, v in store.items():
        if re.match(pattern, k):
            new_store[k] = v
    return new_store

def solve(store, wires):
    covered = [False for _ in wires]
    while not all(covered):
        for i, wire in enumerate(wires):
            n1, op, n2, n3 = wire
            if n1 in store and n2 in store:
                perform_op(n1, op, n2, n3, store)
                covered[i] = True
    store = isolate_store(store)
    bin_str = ''
    for key in sorted(store.keys(), reverse=True):
        bin_str += str(store[key])
    print(int(bin_str, 2))

def part_b():
    store, wires = get_data()
    solve(store, wires)

print('-'*64)
t = time.time()
part_b()
print(f'part b completed in {time.time()-t} seconds')
print('-'*64)

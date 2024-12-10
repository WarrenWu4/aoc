import time
start_time = time.time()

with open('7_input.txt', 'r') as f:
    data = f.read().strip('\n').split('\n')

def foo(prev, i, op, vals, res):
    if i >= len(vals):
        res.append(prev)
        return
    if op == '*':
        new_val = prev*vals[i]
    elif op == '+':
        new_val = prev+vals[i]
    else:
        new_val = int(str(prev)+str(vals[i]))
    foo(new_val, i+1, '*', vals, res)
    foo(new_val, i+1, '+', vals, res)
    foo(new_val, i+1, '||', vals, res)

ans = 0
for line in data:
    [total, eq] = line.split(': ')
    eq = [int(v) for v in eq.split(' ')]
    res = []
    foo(eq[0], 1, '*', eq, res)
    foo(eq[0], 1, '+', eq, res)
    foo(eq[0], 1, '||', eq, res)
    if int(total) in res:
        ans += int(total)
print(ans)

end_time = time.time()
print(f'Completed in {end_time-start_time} s')

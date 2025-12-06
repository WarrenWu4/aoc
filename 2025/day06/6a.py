filename = '6_ex_input.txt'
filename = '6_input.txt'

with open(filename) as f:
  data = f.read().strip('\n').split('\n')

ops = list(data[-1].replace(' ', ''))
res = []
for num in data[0].split(' '):
  if num == '': continue
  res.append(int(num))

for row in data[1:-1]:
  col_num = 0
  for num in row.split(' '):
    if num == '': continue
    if ops[col_num] == '*':
      res[col_num] *= int(num)
    else:
      res[col_num] += int(num)
    col_num += 1
print(sum(res))

def sum_cols(nums):
  total = ''
  for num in nums:
    total += num
  return int(total)

def product(nums):
  total = 1
  for num in nums: total *= num
  return total

filename = '6_ex_input.txt'
filename = '6_input.txt'

with open(filename) as f:
  data = f.read().strip('\n').split('\n')

bounds = []
for i, op in enumerate(data[-1]):
  if op != ' ':
    bounds.append(i)
bounds.append(max([len(row) for row in data])+1)

res = 0
for i in range(len(bounds)-1):
  start, end, ops = bounds[i], bounds[i+1]-1, data[-1][bounds[i]]
  col_nums = []
  for j in range(start, end):
      col_nums.append(sum_cols([row[j] for row in data[:-1]]))
  if ops == '*':
    res += product(col_nums)
  else:
    res += sum(col_nums)
print(res)

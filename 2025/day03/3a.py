filename = '3_ex_input.txt'
filename = '3_input.txt'

with open(filename) as f:
  data = f.read().strip('\n').split('\n')

def find_max_joltage(seq):
  first_max, total_max = -1, 0
  for i in range(len(seq)-1):
    if (first_max > seq[i]):
      continue
    else:
      first_max = seq[i]
    second_max = -1
    for j in range(i+1, len(seq)):
      if (second_max > seq[j]):
        continue
      else:
        second_max = seq[j]
    total_max = max(total_max, first_max * 10 + second_max)
  return total_max 

res = 0
for seq in data:
  res += find_max_joltage([int(num) for num in seq])
print(res)

filename = '3_ex_input.txt'
filename = '3_input.txt'

with open(filename) as f:
  data = f.read().strip('\n').split('\n')

"""
WAIT THIS SHIT IS JUST A STACK BRUH

elements remaining = len(seq) - i - 1
add condition if the stack + elements remaining must be greater than 12 
"""

def find_max_joltage(seq):
  stack = []
  for i, num in enumerate(seq):
    while len(stack) != 0 and stack[-1] < num and len(stack)+len(seq)-i > 12:
      stack.pop()
    if len(stack) < 12:
      stack.append(num)
  return sum([num*10**i for i, num in enumerate(stack[::-1])])

res = 0
for seq in data:
  value = find_max_joltage([int(num) for num in seq])
  res += value
print(res)

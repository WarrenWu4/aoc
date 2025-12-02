# file = '2_ex_input.txt'
file = '2_input.txt'

with open(file) as f:
  ranges = f.read().strip('\n').split(',')

def check_valid(num):
  num_str = str(num)
  n = len(num_str)
  if (n % 2): return True 
  # print(num_str[:n//2], num_str[n//2:])
  return num_str[:n//2] != num_str[n//2:]

res = 0
for nums in ranges:
  start, end = [int(val) for val in nums.split('-')]
  for i in range(start, end+1):    
    if not check_valid(i):
      res += i
print(res)

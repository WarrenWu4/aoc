# file = '2_ex_input.txt'
file = '2_input.txt'

with open(file) as f:
  data = f.read().strip('\n').split(',')

"""
i = 0, prefix = '1'
j = 1, next_num = '2'

i = 1, prefix = '12'
j = 2, next_num = '12'
j = 4, next_num = '12'
"""

def check_valid(num):
  # brute force check
  # create every prefix then check that it matches rest of string
  num_str = str(num)
  n = len(num_str)
  for i in range(n//2):
    prefix = num_str[:i+1]
    repeat = True
    for j in range(i+1, n, len(prefix)):
      next_num = num_str[j:j+len(prefix)]
      if (prefix != next_num):
        repeat = False
        break
    if repeat: 
      # print(prefix)
      return False 
  return True 

# print(check_valid(1212121212))
# print(check_valid(1111111))
# print(check_valid(12341234))
# print(check_valid(123123123))

res = 0
for ranges in data:
  start, end = [int(num) for num in ranges.split('-')]
  for num in range(start, end+1):
    if not check_valid(num):
      # print('Invalid detected:', num)
      res += num
print(res)

filename = '5_ex_input.txt'
filename = '5_input.txt'

with open(filename) as f:
  ranges, ingredients = [l.split('\n') for l in f.read().strip('\n').split('\n\n')]

ingredients = [int(num) for num in ingredients]
ranges = [(int(nums.split('-')[0]), int(nums.split('-')[1])) for nums in ranges]

res = 0
for ingredient in ingredients:
  for start, end in ranges:
    if start <= ingredient <= end:
      res += 1
      break
print(res)


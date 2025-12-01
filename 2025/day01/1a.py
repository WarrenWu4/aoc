with open('1_input.txt') as f:
  data = f.read().strip('\n').split('\n') 

dial_num = 50
res = 0

for value in data:
  dir = 1 if value[0] == 'R' else -1
  num = int(value[1:])
  dial_num = (dial_num + 100 + num * dir) % 100
  res += dial_num == 0 
print(res)

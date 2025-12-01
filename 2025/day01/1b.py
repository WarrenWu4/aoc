with open('1_input.txt') as f:
    data = f.read().strip('\n').split('\n')

'''
Observation: can't determine number of 0s based on initial and final position b/c no telling how many loops were made in between...

would have to look at delta value (how many loops does it make, but it doesn't have to be full loop, just loop at 0)

1. determine whether it crosses based on distance to 0
2. if crosses, then calculate how many times it crosses
> cost_of_initial_cross + 100 for each cross
3. update dial to final destination 

* edge case with cross_dist = 0 b/c it doesn't have an initial cross but could cross multiple times
'''

dial_num = 50
res = 0

for value in data:
  num = int(value[1:])
  cross_dist = 100 - dial_num if value[0] == 'R' else dial_num
  dir = 1 if value[0] == 'R' else -1
  dial_num = (dial_num + 100 + num * dir) % 100
  res += (num - cross_dist) // 100 + (cross_dist != 0) if num > cross_dist else dial_num == 0
print(res)

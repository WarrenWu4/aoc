from collections import defaultdict

with open('2.in', 'r') as f:
    d = f.read().strip().split('\n')

total = 0
for l in d:
    bag_map = defaultdict(int)
    l = l.split(': ')[1].split('; ')
    for bag in l:
        bag = bag.split(', ')
        for cube in bag:
            price, color = cube.split(' ')
            bag_map[color] = max(bag_map[color], int(price))
    total += bag_map['red'] * bag_map['green'] * bag_map['blue']
print(total)
                



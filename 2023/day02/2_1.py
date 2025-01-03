with open('2.in', 'r') as f:
    d = f.read().strip().split('\n')

bag_map = {'red': 12, 'green': 13, 'blue': 14}
total = 0
for l in d:
    valid = int(l.split(': ')[0].split(' ')[1])
    l = l.split(': ')[1].split('; ')
    for bag in l:
        bag = bag.split(', ')
        for cube in bag:
            price, color = cube.split(' ')
            if (int(price) > bag_map[color]):
                valid = 0
    total += valid
print(total)
                


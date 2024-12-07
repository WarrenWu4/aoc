from collections import defaultdict

data = ""
with open("1_input.txt", "r") as f:
    data = f.readlines()
l_list = []
r_list = []
for line in data:
    line = line.strip("\n").split("   ")
    l_list.append(int(line[0]))
    r_list.append(int(line[1]))

counter = defaultdict(int)
for i in range(len(l_list)):
    counter[r_list[i]] += 1

total_similarity = 0
for val in l_list:
    total_similarity += val * counter[val]

print(total_similarity)

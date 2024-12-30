data = ""
with open("1_input.txt", "r") as f:
    data = f.readlines()
l_list = []
r_list = []
for line in data:
    line = line.strip("\n").split("   ")
    l_list.append(int(line[0]))
    r_list.append(int(line[1]))

l_list.sort()
r_list.sort()

total_distance = 0
for i in range(len(l_list)):
    total_distance += abs(l_list[i] - r_list[i])



data = []
with open("2_input.txt", "r") as f:
    for line in f:
        data.append(line.strip("\n").split(" "))
    for i in range(len(data)):
        for j in range(len(data[i])):
            data[i][j] = int(data[i][j])

def check_level(level):
    for idx in range(len(level)-1):
        distance = abs(level[idx]-level[idx+1])
        if (distance < 1 or distance > 3):
            return False
    return (level == sorted(level) or level == sorted(level, reverse=True))

num_safe_reports = 0
for level in data:
    if (check_level(level)): 
        num_safe_reports += 1
print(num_safe_reports)

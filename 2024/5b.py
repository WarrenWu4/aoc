from collections import defaultdict

with open("5_input.txt", "r") as f:
    data = f.read().split("\n\n")
    rules = data[0].split("\n")
    updates = data[1].split("\n")[:-1]

rules_page = defaultdict(list)
for rule in rules:
    [x, y] = rule.split("|")
    rules_page[x].append(y)

ans = 0
for update in updates:
    update = update.split(",")
    update_og = update[:]
    for i in range(len(update)):
        for j in range(len(update)):
            if (update[j] in rules_page[update[i]]):
                temp = update[j]
                update[j] = update[i]
                update[i] = temp
    passes = True
    for val1, val2 in zip(update_og, update):
        if (val1 != val2):
            passes = False
    if (not passes):
        ans += int(update[len(update)//2])
print(ans)





from collections import defaultdict

with open("5_input.txt", "r") as f:
    data = f.read().split("\n\n")
    rules = data[0].split("\n")
    updates = data[1].split("\n")[:-1]

rules_page = defaultdict(list)
for rule in rules:
    [x, y] = rule.split("|")
    rules_page[y].append(x)

ans = 0
for update in updates:
    update = update.split(",")
    passes = True
    for i, val in enumerate(update[:-1]):
        for dependency in rules_page[val]:
            if dependency in update[i+1:]:
                passes = False
    if (passes):
        ans += int(update[len(update)//2])
print(ans)





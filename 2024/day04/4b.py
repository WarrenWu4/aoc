with open("4_input.txt", "r") as f:
    data = f.read().split("\n")[:-1]

total = 0
for row, line in enumerate(data):
    if (row == 0 or row == len(data)-1):
        continue
    for col, char in enumerate(line):
        if (col == 0 or col == len(line)-1):
            continue
        if char == 'A':
            top_left = data[row-1][col-1]
            top_right = data[row-1][col+1]
            bot_left = data[row+1][col-1]
            bot_right = data[row+1][col+1]
            corners = top_left+top_right+bot_left+bot_right
            if ("".join(sorted(corners)) == 'MMSS' and top_left != bot_right and top_right != bot_left):
                total += 1
print(total)

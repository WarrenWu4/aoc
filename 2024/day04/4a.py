with open("4_input.txt", "r") as f:
    data = f.read().split("\n")[:-1]

def check_horizontal(col, line):
    # working so far :P
    backwards = line[max(0, col-3):col+1][::-1]
    forwards = line[col:min(len(line), col+4)]
    truth_arr = [backwards == 'XMAS', forwards == 'XMAS']
    return 2 if all(truth_arr) else 1 if any(truth_arr) else 0

def check_vertical(row, col, data):
    # working so far :P
    top = "".join([line[col] for line in data[max(0, row-3):row+1]])[::-1]
    bottom = "".join([line[col] for line in data[row:min(len(data), row+4)]])
    truth_arr = [top == 'XMAS', bottom == 'XMAS']
    return 2 if all(truth_arr) else 1 if any(truth_arr) else 0

def check_diagonals(row, col, data):
    top = data[max(0, row-3):row+1][::-1]
    bottom = data[row:min(len(data), row+4)]
    top_right = ""
    top_left = ""
    for i, line in enumerate(top):
        if (col+i < len(line)):
            top_right += line[col+i]
        if (col-i >= 0):
            top_left += line[col-i]
    bottom_right = ""
    bottom_left = ""
    for i, line in enumerate(bottom):
        if (col+i < len(line)):
            bottom_right += line[col+i]
        if (col-i >= 0):
            bottom_left += line[col-i]
    truth_arr = [top_right == 'XMAS', top_left == 'XMAS', bottom_right == 'XMAS', bottom_left == 'XMAS']
    return sum(truth_arr)

total = 0
for row, line in enumerate(data):
    for col, char in enumerate(line):
        if char == 'X':
            # check horizontal
            total += check_horizontal(col, line)
            # check vertical
            total += check_vertical(row, col, data)
            # check diagonals
            total += check_diagonals(row, col, data)
print(total)

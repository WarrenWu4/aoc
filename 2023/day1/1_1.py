with open('1.in', 'r') as f:
    data = f.read().strip().split('\n')

digits = [str(i) for i in range(10)]

total = 0
for line in data:
    line_digits = ''
    for num in line:
        if num in digits:
            line_digits += num
            break
    for num in line[::-1]:
        if num in digits:
            line_digits += num
            break
    total += int(line_digits)
print(total)


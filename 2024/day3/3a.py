with open("3_input.txt", "r") as f:
    data = f.read().split("\n")[:-1]
# regex is for pussies
total = 0
for line in data:
    commands = []
    numbers = [str(i) for i in range(10)]
    start_parse = False
    command = ""
    for i, c in enumerate(line):
        if c == '(' and line[max(i-3,0):i] == 'mul':
            start_parse = True
        elif start_parse:
            if c in numbers:
                command += c
            elif c == ',' and c not in command:
                command += c
            elif c == ')':
                commands.append(command)
                command = ""
                start_parse = False
            else:
                command = ""
                start_parse = False
    for c in commands:
        vals = c.split(",")
        if (len(vals) == 2):
            total += int(vals[0]) * int(vals[1])
print(total)

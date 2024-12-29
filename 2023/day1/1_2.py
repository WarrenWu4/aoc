with open('1.in', 'r') as f:
    data = f.read().strip().split('\n')

digits = [str(i) for i in range(10)]
char_digits = {3: ['one', 'two', 'six'],
               4: ['four', 'five', 'nine'],
               5: ['three', 'seven', 'eight']}
word_to_num = {'one': '1', 'two': '2', 'three': '3', 'four': '4', 'five': '5', 'six': '6', 'seven': '7', 'eight': '8', 'nine': '9'}

def get_first_digit(line):
    for i, c in enumerate(line):
        if c in digits:
            return c 
        for k, v in char_digits.items():
            if line[i:i+k] in v:
                return word_to_num[line[i:i+k]]
    return ''

def get_last_digit(line):
    recent = ''
    for i, c in enumerate(line):
        if c in digits:
            recent = c
        for k, v in char_digits.items():
            if line[i:i+k] in v:
                recent = word_to_num[line[i:i+k]]
    return recent

total = 0
for line in data:
    line_digits = get_first_digit(line) + get_last_digit(line)
    total += int(line_digits)
print(total)


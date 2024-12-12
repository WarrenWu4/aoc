import time
from collections import defaultdict

with open('input.txt', 'r') as f:
    data = f.read().strip('\n').split('\n')

def part_a(data):
    disallowed = ['ab', 'cd', 'pq', 'xy']
    nice = 0
    for line in data:    
        vowels = {'a':0, 'e':0, 'i':0, 'o':0, 'u':0}
        passes = False
        for i in range(0, len(line)-1):
            sub = line[i:i+2]
            if (sub[0] in vowels):
                vowels[sub[0]] += 1
            if (sub[0] == sub[1]):
                passes = True
            if sub in disallowed:
                passes = False
                break
        if line[-1] in vowels:
            vowels[line[-1]] += 1
        if sum(vowels.values()) < 3:
            passes = False
        if (passes):
            nice += 1
    print(nice)

def part_b(data):
    nice = 0
    for line in data:
        passes = [False, False] 
        for i in range(len(line)-1):
            test = line[i:i+2]
            if test in line[i+2:]:
                passes[0] = True
        for i in range(len(line)-2):
            if line[i] == line[i+2]:
                passes[1] = True
                break
        if (all(passes)):
            nice += 1
    print(nice)

start_time = time.time()
part_a(data)
end_time = time.time()
print(f'part a completed in {end_time-start_time}')

start_time = time.time()
part_b(data)
end_time = time.time()
print(f'part b completed in {end_time-start_time}')

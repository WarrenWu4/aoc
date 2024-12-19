import time

def get_data(filename='17.in'):
    with open(filename, 'r') as f:
        registers, program = f.read().strip('\n').split('\n\n')
        registers = [l for l in registers.split('\n')]
    prog, reg = [], {}
    for register in registers:
        register = register.split(' ')
        reg[register[1][0]] = int(register[2])
    prog = [int(n) for n in program.split(' ')[1].split(',')]
    return prog, reg


def get_combo_operand(operand, registers):
    op_to_reg = {4:'A', 5:'B', 6:'C'}
    return operand if (0 <= operand <= 3) else registers[op_to_reg[operand]]

def compute(opcode, operand, registers, instruction_pointer, out):
    if opcode == 0:
        registers['A'] = int(registers['A'] / 2**get_combo_operand(operand, registers))
    elif opcode == 1:
        registers['B'] = registers['B'] ^ operand
    elif opcode == 2:
        registers['B'] = get_combo_operand(operand, registers) % 8
    elif opcode == 3:
        if registers['A'] != 0:
            return operand 
    elif opcode == 4:
        registers['B'] = registers['B'] ^ registers['C']
    elif opcode == 5:
        out.extend(list(f'{get_combo_operand(operand, registers) % 8}'))
    elif opcode == 6:
        registers['B'] = int(registers['A'] / 2**get_combo_operand(operand, registers))
    else:
        registers['C'] = int(registers['A'] / 2**get_combo_operand(operand, registers))
    return instruction_pointer + 2

def part_a(data):
    prog, reg = data
    ptr = 0
    output = []
    while (ptr < len(prog) - 1):
        ptr = compute(prog[ptr], prog[ptr+1], reg, ptr, output)
    print(','.join(output))

def part_b(data):
    prog, reg = data
    ptr = 0

print(f'{'-'*16}')
t = time.time()
part_a(get_data('17.in'))
print(f'part a completed in {time.time()-t} sec\n{'-'*16}')

t = time.time()
part_b(get_data('a.in'))
print(f'part b completed in {time.time()-t} sec\n{'-'*16}')

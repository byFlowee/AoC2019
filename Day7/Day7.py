import time
from itertools import permutations

def parse_input(fname):
    return [int(x) for x in open(fname, 'r').read().split(',')]

program = parse_input('Day7/input')

def compute_amplifiers_output():
    max_thrust = 0
    for perms in permutations(range(0,5)):
        output = run(perms[0], 0)
        for sequence in perms[1::]:
            output = run(sequence, output[-1])
        if output[0] > max_thrust:
            max_thrust = output[0]
            print(output)

def run(sequence, amplifier_input):
    it = 0
    output = []
    input_counter = 0

    while (True):
        op = [int(char) for char in str(program[it]).zfill(5)]

        if op[4] == 1:
            program[program[it+3]] = (program[program[it+1]] if op[2] == 0 else program[it+1]) + (program[program[it+2]] if op[1] == 0 else program[it+2])
            it += 4
        elif op[4] == 2:
            program[program[it+3]] = (program[program[it+1]] if op[2] == 0 else program[it+1]) * (program[program[it+2]] if op[1] == 0 else program[it+2])
            it += 4
        elif op[4] == 3:
            program[program[it+1]] = sequence if input_counter == 0 else amplifier_input
            input_counter += 1
            it += 2
        elif op[4] == 4:
            output.append(program[program[it+1]] if op[2] == 0 else program[it+1])
            it += 2
        elif op[4] == 5:
            if (program[program[it+1]] if op[2] == 0 else program[it+1]) != 0:
                it = program[program[it+2]] if op[1] == 0 else program[it+2]
            else:
                it += 3
        elif op[4] == 6:
            if (program[program[it+1]] if op[2] == 0 else program[it+1]) == 0:
                it = program[program[it+2]] if op[1] == 0 else program[it+2]
            else:
                it += 3
        elif op[4] == 7:
            if (program[program[it+1]] if op[2] == 0 else program[it+1]) < (program[program[it+2]] if op[1] == 0 else program[it+2]):
                program[program[it+3]] = 1
            else:
                program[program[it+3]] = 0
            it += 4
        elif op[4] == 8:
            if (program[program[it+1]] if op[2] == 0 else program[it+1]) == (program[program[it+2]] if op[1] == 0 else program[it+2]):
                program[program[it+3]] = 1
            else:
                program[program[it+3]] = 0
            it += 4
        elif op[4] == 9:
            return output

#run()
compute_amplifiers_output()
import time

def parse_input(fname):
    return [int(x) for x in open(fname, 'r').read().split(',')]

program = parse_input('input')

def run():
    it = 0
    while (True):
        op = [int(char) for char in str(program[it]).zfill(5)]
        
        if op[4] == 1:
            program[program[it+3]] = (program[program[it+1]] if op[2] == 0 else program[it+1]) + (program[program[it+2]] if op[1] == 0 else program[it+2])
            it += 4
        elif op[4] == 2:
            program[program[it+3]] = (program[program[it+1]] if op[2] == 0 else program[it+1]) * (program[program[it+2]] if op[1] == 0 else program[it+2])
            it += 4
        elif op[4] == 3:
            program[program[it+1]] = int(input('Input: ')) 
            it += 2
        elif op[4] == 4:
            print(program[program[it+1]] if op[2] == 0 else program[it+1])
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
            return program[0]

run()
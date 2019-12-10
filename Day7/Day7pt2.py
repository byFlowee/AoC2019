import time
from itertools import permutations

def parse_input(fname):
    return [int(x) for x in open(fname, 'r').read().split(',')]

programs = []
for _ in range(5):
    programs.append(parse_input('Day7/input'))

amplifiers_output = [[0],[0],[0],[0],[0]]
amplifiers_pointer = [0] * 5

def reset_input_program():
    global programs
    for i in range(5): 
        programs[i] = parse_input('Day7/input')

def compute_amplifiers_feedback():
    maximum_signal = 0
    for perm in permutations(range(5,10)):
        reset_input_program()
        for opt in amplifiers_output:
            opt.clear()
            opt.append(0)
        for idx in range(len(amplifiers_pointer)):
            amplifiers_pointer[idx] = 0
        
        loop_id = 0
        while amplifiers_pointer[-1] != -1:
            for idx, sequence in enumerate(perm):
                run(sequence, amplifiers_pointer[idx], idx, loop_id)
            
            loop_id += 1
        
        if max(amplifiers_output[-1]) > maximum_signal:
            maximum_signal = max(amplifiers_output[-1])

    return maximum_signal
                

def run(sequence, it, idx, loop_id):
    wait_for_next = False
    feed_sequence = True

    while (True):
        op = [int(char) for char in str(programs[idx][it]).zfill(5)]

        if op[4] == 1:
            programs[idx][programs[idx][it+3]] = (programs[idx][programs[idx][it+1]] if op[2] == 0 else programs[idx][it+1]) + (programs[idx][programs[idx][it+2]] if op[1] == 0 else programs[idx][it+2])
            it += 4
        elif op[4] == 2:
            programs[idx][programs[idx][it+3]] = (programs[idx][programs[idx][it+1]] if op[2] == 0 else programs[idx][it+1]) * (programs[idx][programs[idx][it+2]] if op[1] == 0 else programs[idx][it+2])
            it += 4
        elif op[4] == 3:
            if wait_for_next:
                amplifiers_pointer[idx] = it
                return
            if loop_id == 0 and feed_sequence:
                programs[idx][programs[idx][it+1]] = sequence
                feed_sequence = False
                it += 2
            else:
                feedback_from = (idx - 1) % 5 
                programs[idx][programs[idx][it+1]] = amplifiers_output[feedback_from][-1]
                wait_for_next = True
                it += 2
        elif op[4] == 4:
            amplifiers_output[idx].append(programs[idx][programs[idx][it+1]] if op[2] == 0 else programs[idx][it+1])
            it += 2
        elif op[4] == 5:
            if (programs[idx][programs[idx][it+1]] if op[2] == 0 else programs[idx][it+1]) != 0:
                it = programs[idx][programs[idx][it+2]] if op[1] == 0 else programs[idx][it+2]
            else:
                it += 3
        elif op[4] == 6:
            if (programs[idx][programs[idx][it+1]] if op[2] == 0 else programs[idx][it+1]) == 0:
                it = programs[idx][programs[idx][it+2]] if op[1] == 0 else programs[idx][it+2]
            else:
                it += 3
        elif op[4] == 7:
            if (programs[idx][programs[idx][it+1]] if op[2] == 0 else programs[idx][it+1]) < (programs[idx][programs[idx][it+2]] if op[1] == 0 else programs[idx][it+2]):
                programs[idx][programs[idx][it+3]] = 1
            else:
                programs[idx][programs[idx][it+3]] = 0
            it += 4
        elif op[4] == 8:
            if (programs[idx][programs[idx][it+1]] if op[2] == 0 else programs[idx][it+1]) == (programs[idx][programs[idx][it+2]] if op[1] == 0 else programs[idx][it+2]):
                programs[idx][programs[idx][it+3]] = 1
            else:
                programs[idx][programs[idx][it+3]] = 0
            it += 4
        elif op[4] == 9:
            amplifiers_pointer[idx] = -1
            return

#run()
print(compute_amplifiers_feedback())
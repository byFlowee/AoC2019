import time
from enum import Enum
import numpy as np
from matplotlib import pyplot as plt

def parse_input(fname):
    mem = [int(x) for x in open(fname, 'r').read().split(',')]
    for _ in range(1000):
        mem.append(0)
    return mem

WIDTH  = 37
HEIGHT = 22

program = parse_input('Day13/input')
grid = [[0 for y in range(WIDTH)] for x in range(HEIGHT)]

def get_param(mode, it, b):
    if mode == 2:
        return program[b + program[it]]
    if mode == 1:
        return program[it]
    if mode == 0:
        return program[program[it]]

def write_to(mode, it, b, val):
    if mode == 2:
        program[b + program[it]] = val
    if mode == 0:
        program[program[it]] = val

def run(it, b, move):
    r_base = b
    out_count = 0
    out = []

    while (True):
        op = [0] * 5
        n = program[it]
        for i in range(5):
            op[i] = n % 10
            n //= 10
        
        if op[0] == 1:
            write_to(op[4], it+3, r_base, get_param(op[2],it+1,r_base) + get_param(op[3],it+2,r_base))
            it += 4
        elif op[0] == 2:
            write_to(op[4], it+3, r_base, get_param(op[2],it+1,r_base) * get_param(op[3],it+2,r_base))
            it += 4
        elif op[0] == 3:
            write_to(op[2], it+1, r_base, move)
            print('move: {}'.format(move))
            it += 2
        elif op[0] == 4:
            out.append(get_param(op[2],it+1,r_base))
            it += 2
            out_count += 1
            if out_count == 3:
                return out, it, r_base
        elif op[0] == 5:
            if get_param(op[2],it+1,r_base) != 0:
                it = get_param(op[3],it+2,r_base)
            else:
                it += 3
        elif op[0] == 6:
            if get_param(op[2],it+1,r_base) == 0:
                it = get_param(op[3],it+2,r_base)
            else:
                it += 3
        elif op[0] == 7:
            if get_param(op[2],it+1,r_base) < get_param(op[3],it+2,r_base):
                write_to(op[4], it+3, r_base, 1)
            else:
                write_to(op[4], it+3, r_base, 0)
            it += 4
        elif op[0] == 8:
            if get_param(op[2],it+1,r_base) == get_param(op[3],it+2,r_base):
                write_to(op[4], it+3, r_base, 1)
            else:
                write_to(op[4], it+3, r_base, 0)
            it += 4
        elif op[0] == 9 and op[1] == 9:
            return None, it, r_base
        elif op[0] == 9:
            r_base += get_param(op[2],it+1,r_base)
            it += 2

def draw_thingy():
    ptr = 0
    b = 0
    move = 0
    paddle = 0

    plt.ion()
    fig = plt.figure()

    for _ in range(813):
        v, ptr, b = run(ptr, b, _)
        grid[v[1]][v[0]] = v[2]
        
        if v[2] == 3:
            paddle = v[0]

    while (True):
        v, ptr, b = run(ptr, b, move)

        if not v:
            break
        
        if v[0] == -1 and v[1] == 0:
            print('Score: {}'.format(v[2]))
        else:
            grid[v[1]][v[0]] = v[2]
        
        if v[2] == 4:
            if v[0] > paddle:
                move = 1
                paddle += 1
            elif v[0] < paddle:
                move = -1
                paddle -= 1
            else:
                move = 0

        plt.imshow(grid)
        plt.show()
        plt.pause(0.05)
        
program[0] = 2

draw_thingy()
print(sum([row.count(2) for row in grid]))


#run(0)
import time
from enum import Enum

def parse_input(fname):
    mem = [int(x) for x in open(fname, 'r').read().split(',')]
    for _ in range(10000):
        mem.append(0)
    return mem

WIDTH  = 10000
HEIGHT = 10000

class Direction(Enum):
    up = [-1, 0]
    right = [0, 1]
    left = [0, -1]
    down = [1, 0]

program = parse_input('Day11/input')
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
    if mode == 1:
        program[it] = val

def run(panel, it):
    r_base = 0
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
            write_to(op[2], it+1, r_base, panel)
            it += 2
        elif op[0] == 4:
            out.append(get_param(op[2],it+1,r_base))
            it += 2
            out_count += 1
            if out_count == 2:
                return out, it
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
            return None, it
        elif op[0] == 9:
            r_base += get_param(op[2],it+1,r_base)
            it += 2

def painting_robot_thingy():
    x, y = WIDTH//2, HEIGHT//2
    ptr = 0
    current_dir = Direction.up

    while (True):
        v, ptr = run(grid[x][y], ptr)
        if not v:
            return

        grid[x][y] = v[0]

        if current_dir == Direction.up:
            current_dir = Direction.left if v[1] == 0 else Direction.right
        elif current_dir == Direction.right:
            current_dir = Direction.up if v[1] == 0 else Direction.down
        elif current_dir == Direction.down:
            current_dir = Direction.right if v[1] == 0 else Direction.left
        elif current_dir == Direction.left:
            current_dir = Direction.up if v[1] == 0 else Direction.down
        
        x += current_dir.value[0]
        y += current_dir.value[1]

        

        
painting_robot_thingy()

print(grid)
#run(0)
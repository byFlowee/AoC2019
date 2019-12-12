import re
from copy import deepcopy
from itertools import combinations

class Moon:

    def __init__(self, coords):
        self.coords = [0,0,0]
        self.speed  = [0,0,0]
        self.coords[0] = coords[0]
        self.coords[1] = coords[1]
        self.coords[2] = coords[2]

    def apply_gravity(self, other):
        if self.coords[0] != other.coords[0]:
            grav = 1 if self.coords[0] < other.coords[0] else -1
            self.speed[0] += grav
            other.speed[0] += -grav

        if self.coords[1] != other.coords[1]:
            grav = 1 if self.coords[1] < other.coords[1] else -1
            self.speed[1] += grav
            other.speed[1] += -grav

        if self.coords[2] != other.coords[2]:
            grav = 1 if self.coords[2] < other.coords[2] else -1
            self.speed[2] += grav
            other.speed[2] += -grav

    def apply_velocity(self):
        self.coords[0] += self.speed[0]
        self.coords[1] += self.speed[1]
        self.coords[2] += self.speed[2]

    def get_coords(self):
        return (self.coords[0], self.coords[1], self.coords[2])

    def get_speed(self):
        return (self.speed[0], self.speed[1], self.speed[2])

    def compute_energy(self):
        return (abs(self.coords[0]) + abs(self.coords[1]) + abs(self.coords[2])) * (abs(self.speed[0]) + abs(self.speed[1]) + abs(self.speed[2]))

    def __str__(self):
        return 'pos=<x={}, y={}, z={}>, vel=<x={}, y={}, z={}>'.format(self.coords[0], self.coords[1], self.coords[2], self.speed[0], self.speed[1], self.speed[2])

    def __eq__(self, other):
        return self.coords[0] == other.coords[0] and self.coords[1] == other.coords[1] and self.coords[2] == other.coords[2] and self.speed[0] == other.speed[0] and self.speed[1] == other.speed[1] and self.speed[3] == other.speed[2] 

def parse_input():
    moons = []
    with open('Day12/input', 'r') as f:
        for l in f:
            moons.append(Moon([int(x) for x in re.findall(r'[-]?\d+', l)]))

    return moons

moons = parse_input()

"""
Part1

for _ in range(1000):
    for pair in combinations(moons, 2):
        pair[0].apply_gravity(pair[1])

    for m in moons:
        m.apply_velocity()

print(sum([m.compute_energy() for m in moons]))
"""

initial_state = deepcopy(moons)

state = [{}]*3
cycle = [0]*3

step = 0
while(True):
    for pair in combinations(moons, 2):
        pair[0].apply_gravity(pair[1])

    for m in moons:
        m.apply_velocity()
    
    for i in range(3):
        if cycle[i]:
            continue
        
        x = tuple([m.coords[i] for m in moons] + [m.speed[i] for m in moons])

        if x in state[i]:
            cycle[i] = step
            print(f'cycle {i} {step}')
        else:
            state[i][x] = None
    
    if all(cycle):
        break

    step += 1


            



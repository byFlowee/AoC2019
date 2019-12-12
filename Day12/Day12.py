import re
from copy import deepcopy
from itertools import combinations

class Moon:
    x = 0
    y = 0
    z = 0

    vx = 0
    vy = 0 
    vz = 0

    def __init__(self, coords):
        self.x = coords[0]
        self.y = coords[1]
        self.z = coords[2]

    def apply_gravity(self, other):
        if self.x != other.x:
            grav = 1 if self.x < other.x else -1
            self.vx += grav
            other.vx += -grav

        if self.y != other.y:
            grav = 1 if self.y < other.y else -1
            self.vy += grav
            other.vy += -grav

        if self.z != other.z:
            grav = 1 if self.z < other.z else -1
            self.vz += grav
            other.vz += -grav

    def apply_velocity(self):
        self.x += self.vx
        self.y += self.vy
        self.z += self.vz

    def get_coords(self):
        return (self.x, self.y, self.z)

    def get_speed(self):
        return (self.vx, self.vy, self.vz)

    def compute_energy(self):
        return (abs(self.x) + abs(self.y) + abs(self.z)) * (abs(self.vx) + abs(self.vy) + abs(self.vz))

    def __str__(self):
        return 'pos=<x={}, y={}, z={}>, vel=<x={}, y={}, z={}>'.format(self.x, self.y, self.z, self.vx, self.vy, self.vz)

    def __eq__(self, other):
        return self.x == other.x and self.y == other.y and self.z == other.z and self.vx == other.vx and self.vy == other.vy and self.vz == other.vz 

def parse_input():
    moons = []
    with open('Day12/input', 'r') as f:
        for l in f:
            moons.append(Moon([int(x) for x in re.findall(r'[-]?\d+', l)]))

    return moons

moons = parse_input()
initial_state = deepcopy(moons)

for pair in combinations(moons, 2):
    pair[0].apply_gravity(pair[1])

for m in moons:
    m.apply_velocity()

step = 2
while(True):
    skip = False
    for pair in combinations(moons, 2):
        pair[0].apply_gravity(pair[1])

    for m in moons:
        m.apply_velocity()
    
    for m in moons:
        if m.get_speed() != (0,0,0):
           break 
    else:
        print('cycle, {}'.format(step))

    for m1,m2 in zip(moons, initial_state):
        if m1 != m2:    
            skip = True
            break
    
    if not skip:
        print(step)
        break
    
    step += 1
            
"""
print(sum([m.compute_energy() for m in moons]))
"""
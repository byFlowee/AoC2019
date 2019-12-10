import sys
import numpy as np

def parse_file(filename):
    with open(filename, 'r') as f:
        wires = [[],[]]
        A, B = f.read().split('\n')
        
        for idx, n in enumerate([A, B]):
            wires[idx] = n.split(',')

    return wires

def instructions_to_coord(wires):
    wire_coords = []

    for wire in wires:
        coords = [[0, 0]]
        current = [0,0]
        
        for instruction in wire:
            if instruction[0] == 'R':
                current = [current[0], current[1] + int(instruction[1:])]            
                coords.append(current)
            elif instruction[0] == 'L':
                current = [current[0], current[1] - int(instruction[1:])]
                coords.append(current)
            elif instruction[0] == 'U':
                current = [current[0] + int(instruction[1:]), current[1]]
                coords.append(current)
            elif instruction[0] == 'D':
                current = [current[0] - int(instruction[1:]), current[1]]
                coords.append(current)
            else:
                print('bruh momoment')
        
        wire_coords.append(coords)

    return wire_coords            

def compute_intersection(a1, a2, b1, b2):
    collisions = []

    print(f'{a1}{a2}{b1}{b2}')

    """
    if a1[0] <= b1[0] and a2[0] >= b2[0]:
        if b1[1] >= a1[1] and b2[1] <= a2[1]:
            collisions.append([a1[0],b1[1]])
            print(f'\t intersect: {collisions}')
    """
    
    s = np.vstack([a1,a2,b1,b2])        # s for stacked
    h = np.hstack((s, np.ones((4, 1)))) # h for homogeneous
    l1 = np.cross(h[0], h[1])           # get first line
    l2 = np.cross(h[2], h[3])           # get second line
    x, y, z = np.cross(l1, l2)          # point of intersection
    if z == 0:                          # lines are parallel
        return collisions
    
    print([int(x//z), int(y//z)])
    collisions = collisions.append([int(x//z), int(y//z)])
    print(collisions)
    
    return collisions

def compute_all_collisions(coords):
    
    all_collisions = []
    
    for segment_a, next_segment_a in zip(coords[0], coords[0][1::]):
        for segment_b, next_segment_b in zip(coords[1], coords[1][1::]):
            collisions = compute_intersection(segment_a, next_segment_a, segment_b, next_segment_b)
            print(collisions)
            if collisions:
                all_collisions.append(collisions[0])


    return all_collisions

def compute_closest_point(collisions):
    solution = sys.maxsize
    closest_point = []

    for point in collisions:
        distance = abs(point[0]) + abs(point[1])
        
        if distance < solution:
            solution = distance
            closest_point = point

    return solution, closest_point 

def compute_cost(wire, intersection):
    cost = 0
    
    for point, next_point in zip(wire, wire[1::]):
        if compute_intersection(point, next_point, intersection, intersection):
            return cost
        else:
            cost += max(abs(point[0] - next_point[0]), abs(point[1] - next_point[1]))

    return 0

def min_cost_intersection(wire1, wire2, intersections):
    minimum_cost = sys.maxsize

    for intersection in intersections:
        total = compute_cost(wire1, intersection) + compute_cost(wire2, intersection)
        if total < minimum_cost:
            minimum_cost = total

    return minimum_cost

if __name__ == "__main__":
    wires = parse_file("input2.txt")
    coords1 = instructions_to_coord(wires)
    all_points = compute_all_collisions(coords1)
    print(all_points)

    print(compute_closest_point(all_points[1:]))


    #print(min_cost_intersection(coords1[0], coords1[1], all_points))
    
    #print(compute_intersection([10,20],[10,-15],[10,-30],[10,-10]))

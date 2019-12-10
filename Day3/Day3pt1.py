import sys

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
        coords = []
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
                AssertionError('bruh momoment')
        
        wire_coords.append(coords)

    return wire_coords            

def compute_intersection(a1, a2, b1, b2):
    collisions = []
    
    A = 0 if a1[0] != a2[0] else 1
    B = 0 if b1[0] != b2[0] else 1

    if B != A:
        if a1[A] <= b1[A] and a2[A] >= b2[A]:
            if b1[B] >= a1[B] and b2[B] <= a2[B]:
                print(f'A {A}, B {B}: {a1} {a1} {b1} {b2}')
                if A == 1:
                    print('swap!')
                    A = 0
                    B = 1

                collisions.append([a1[A],b1[B]])
    
    return collisions
    """            
    else:
        A = 1 if B == 0 else 0
        if (a1[A] == a2[A] and b1[A] == b2[A]):
            print(f'colision in axis{B}: {b1[B]} {b2[B]} {a1[B]} {a2[B]}')

            i1, i2 = (b1[B], b2[B]) if b1[B] < b2[B] else (b2[B], b1[B])
            j1, j2 = (a1[B], a2[B]) if a1[B] < a2[B] else (a2[B], a1[B])

            for coord in list(set(range(i1, i2+1)) & set(range(j1,j2+1))):
                collisions.append([a1[A],coord] if A == 0 else [coord,a1[A]])
            
            return collisions
    """
def compute_all_collisions(coords):
    
    all_collisions = []
    
    for segment_a, next_segment_a in zip(coords[0], coords[0][1::]):
        for segment_b, next_segment_b in zip(coords[1], coords[1][1::]):
            collisions = compute_intersection(segment_a, next_segment_a, segment_b, next_segment_b)
            if collisions:
                all_collisions.append(collisions[0])


    return all_collisions

def compute_closest_point(collisions):
    solution = sys.maxsize
    
    for point in collisions:
        distance = abs(point[0]) + abs(point[1])
        
        if distance < solution:
            solution = distance

    return solution

if __name__ == "__main__":
    wires = parse_file("input.txt")
    coords1 = instructions_to_coord(wires)
    all_points = compute_all_collisions(coords1)
    
    #print(compute_closest_point(all_points))
    
    #print(compute_intersection([10,20],[10,-15],[10,-30],[10,-10]))

def parse_input():
    return [[y for y in x] for x in open('input', 'r').read().split('\n')]

data = parse_input()

# y = mx + c 
def trace_line(x1,y1,x2,y2):

    # same points
    if x1 == x2 and y1 == y2:
        return ()

    # slope is zero, collision is along y axis
    if x1 == x2:
        step = 1 if y1 < y2 else -1
        for y in range(y1+step, y2+step, step):
            #print(x1, y)
            if data[y][x1] == '#':
                return (x1,y)

        return ()

    m = (y2 - y1) / (x2 - x1)
    c = y1 - m*x1

    step = 1 if x1 < x2 else -1
    for bruh in range(x1+step, x2+step, step):
        y = m*bruh + c
        y = round(y,ndigits=4)
        if y.is_integer():
            if data[int(y)][bruh] == '#':
                return (bruh, int(y))

    return ()            

def compute_observable_asteroids(x, y):
    visible = set()
    for chocho in range(len(data)):
        for ojete in range(len(data[0])):
            if data[ojete][chocho] == '#':
                visible.add(trace_line(x,y,chocho,ojete))    

    return len(visible) - 1
    
def get_max_visible():
    best = 0
    best_xy = (0,0)
    for current_x in range(len(data)):
        for current_y in range(len(data[0])):
            if data[current_y][current_x] == '#':
                n = compute_observable_asteroids(current_x, current_y)
                if n > best:
                    best = n
                    best_xy = (current_x, current_y)  

    return best_xy, best

def laser_de_muerte_rotatorio():
    pass

#compute_observable_asteroids(5,8)

print(get_max_visible())
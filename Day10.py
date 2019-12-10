def parse_input():
    return [[y for y in x] for x in open('test', 'r').read().split('\n')]

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
    for i in range(len(data)):
        visible.add(trace_line(x,y,i,0))
        visible.add(trace_line(x,y,i,len(data[0])-1))
    for j in range(len(data[0])):
        visible.add(trace_line(x,y,0,j))
        visible.add(trace_line(x,y,len(data)-1, j))
    
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

#compute_observable_asteroids(4,2)

print(get_max_visible())
import numpy as np
from matplotlib import pyplot as plt

def parse_input():
    return [x for x in open('Day8/input', 'r').read()]

def compute_layers(data):
    num_layers = len(data) // (25*6)
    arranged = np.zeros([num_layers, 6, 25], dtype=np.uint8)
    data_ptr = 0
    for layer in range(num_layers):
        for width in range(6):
            for height in range(25):
                arranged[layer][width][height] = int(data[data_ptr])
                data_ptr += 1
    
    return arranged

img = compute_layers(parse_input())

min_zero_layer = -1
min_zeros = 25*6

for idx, layer in enumerate(img):
    zero_count = 0
    for row in layer:
        for pixel in row:
            if pixel == 0:
                zero_count += 1

    if zero_count < min_zeros:
        min_zeros = zero_count
        min_zero_layer = idx

print(min_zeros)
print(min_zero_layer)

one_count = 0
two_count = 0

for row in img[5]:
    for pixel in row:
        if pixel == 1:
            one_count += 1
        elif pixel == 2:
            two_count += 1

print(one_count*two_count)

#img = np.reshape(img, [25,6,100])

end_layer = np.full([1, 6, 25], 2, dtype=np.uint8)
for layer in img:
    for i,row in enumerate(layer):
        for j,pixel in enumerate(row):
            if pixel != 2 and end_layer[0][i][j] == 2:
                end_layer[0][i][j] = pixel
                print(end_layer)

plt.imshow(end_layer[0])
plt.show() 
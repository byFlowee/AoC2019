import re
import math

rd = {}
stock = {}

def parse_input():
    for x in open('Day14/input', 'r').read().split('\n'):
        reaction = re.findall(r'\d+ [A-Z]+', x)
        test = reaction[-1].split(' ')
        rd[ test[-1] ] = [tuple(y.split(' ')) for y in reaction[:-1]]
        rd[ test[-1] ].append(int(test[0]))
        stock[ test[-1] ] = 0

parse_input()

def min_cost_reaction(res):
    if res[1] == 'ORE':
        return int(res[0])

    if int(res[0]) % rd[res[1]][-1] != 0:
        num_reactions = math.ceil(int(res[0]) / rd[res[1]][-1])
        extra = (rd[res[1]][-1] * num_reactions) - int(res[0])

    cost = 0
    for x in rd[res[1]][:-1]:
        cost += min_cost_reaction(x) * num_reactions
    
    return cost

print(min_cost_reaction(('1', 'FUEL')))
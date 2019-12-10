import sys
from collections import defaultdict

def parse_input():
    return [x.split(')') for x in open('Day6/bigboy1M.txt', 'r').read().split('\n')]

def parse2():
    dictionary = {}
    with open("Day6/bigboy1M.txt") as f:
        for x in f:
            k, v = x[:5], x[6:11]
            dictionary[k] = dictionary.get(k, []) + [v]
    return dictionary

def list_to_dict(lst):
    dictionary = {}
    
    for k, v in lst:
        dictionary[k] = dictionary.get(k, []) + [v]

    return dictionary

def compute_stuff(first, current_cost):
    if first not in orbits:
        return current_cost
    if len(orbits[first]) > 1:
        total = current_cost
        for x in orbits[first]:
            total += compute_stuff(x, current_cost + 1)
        return total
    if len(orbits[first]) == 1:
        return current_cost + compute_stuff(orbits[first][0], current_cost + 1)

def cost_to(obj, target, cost):
    if cost >= poda:
        return 0
    if obj == target:
        return cost
    if obj in orbits:
        if len(orbits[obj]) == 1:
            return cost_to(orbits[obj][0], target, cost + 1)

        chocho = sys.maxsize
        for x in orbits[obj]:
            foo = cost_to(x, target, cost + 1)
            if foo != 0 and foo < chocho:
                chocho = foo

        return chocho

    return 0

def min_orbital_transfer(you, san):
    min_cost = sys.maxsize

    for k, _ in orbits.items():
        cost1, cost2 = cost_to(k, san, 0), cost_to(k, you, 0)
        if cost1 == 0 or cost2 == 0:
            continue
        total = cost1 + cost2
        if total < min_cost:
            min_cost = total

    return min_cost - 2

#orbits = list_to_dict(parse_input())
orbits = parse2()
compute_stuff('COM', 0)

poda = sys.maxsize
print(min_orbital_transfer('YOU', 'SAN'))
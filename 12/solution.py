from collections import defaultdict
from functools import cache

with open('input.txt') as f:
    data = f.read()

connections = defaultdict(list)

for line in data.splitlines():
    f, t = line.split('-')
    connections[f].append(t)
    connections[t].append(f)


@cache
def paths_to_end(current, visited, strict_mode):
    if current == 'end':
        return 1
    
    if current in visited and current.islower():
        if current == 'start' or strict_mode:
            return 0
        strict_mode = True

    visited = frozenset([*visited, current])
    return sum(
        paths_to_end(n, visited, strict_mode)
        for n in connections[current]
    )


print("Part 1:", paths_to_end('start', frozenset(), True)) # 3887
print("Part 2:", paths_to_end('start', frozenset(), False)) # 104834

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
def paths_to_end(current, visited, with_slack):
    if current == 'end':
        return 1
    
    if current in visited and current.islower():
        if not with_slack or current == 'start':
            return 0
        with_slack = False

    visited = frozenset([*visited, current])
    return sum(
        paths_to_end(n, visited, with_slack)
        for n in connections[current]
    )


print("Part 1:", paths_to_end('start', frozenset(), False)) # 3887
print("Part 2:", paths_to_end('start', frozenset(), True)) # 104834

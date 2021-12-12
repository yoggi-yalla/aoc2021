from collections import defaultdict

with open('input.txt') as f:
    data = f.read()

connections = defaultdict(list)

for line in data.splitlines():
    f, t = line.split('-')
    connections[f].append(t)
    connections[t].append(f)


def paths_to_end(current, visited, slack):
    if current == 'end':
        return 1
    
    if current in visited and current.islower():
        if current == 'start':
            return 0
        elif not slack:
            return 0
        else:
            slack = 0

    visited[current] += 1
    return sum(
        paths_to_end(n, visited.copy(), slack)
        for n in connections[current]
    )


print("Part 1:", paths_to_end('start', defaultdict(int), 0)) # 3887
print("Part 2:", paths_to_end('start', defaultdict(int), 1)) # 104834

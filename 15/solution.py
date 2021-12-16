from collections import defaultdict

with open('input.txt') as f:
    data = f.read()

grid_1 = [[int(c) for c in line] for line in data.splitlines()]

directions = [
    ( 1, 0),
    ( 0, 1),
    (-1, 0),
    ( 0,-1)
]

def is_out_of_bounds(x, y, size):
    return x >= size or y >= size or x < 0 or y < 0

def run(grid):
    size = len(grid)

    visited = set()
    cost_map = defaultdict(lambda: float('inf'))
    cost_map[(0, 0)] = 0

    while cost_map:
        x, y = min(cost_map, key=cost_map.get)
        visited.add((x, y))
        cost = cost_map.pop((x, y))
        for dx, dy in directions:
            x2, y2 = x + dx, y + dy
            if (x2, y2) in visited or is_out_of_bounds(x2, y2, size):
                continue
            added_cost = grid[x2][y2]
            cost_map[(x2, y2)] = min(cost_map[(x2, y2)], cost + added_cost)

    return cost

print("Part 1:", run(grid_1))


grid_2 = []
for line in grid_1:
    new_line = []
    for i in range(5):
        for num in line:
            new_num = (num + i)
            if new_num > 9:
                new_num = new_num % 9
            new_line.append(new_num)
    grid_2.append(new_line)

additions = []
for i in range(1, 5):
    for line in grid_2:
        new_line = []
        for num in line:
            new_num = (num + i)
            if new_num > 9:
                new_num = new_num % 9
            new_line.append(new_num)
        additions.append(new_line)
grid_2 += additions

print("Part 2:", run(grid_2,)) # 2897

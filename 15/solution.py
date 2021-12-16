import heapq

with open('input.txt') as f:
    data = f.read()

directions = [
    ( 1, 0),
    ( 0, 1),
    (-1, 0),
    ( 0,-1)
]

def neighbors(x, y):
    for dx, dy in directions:
        yield (x + dx, y + dy)

def run(grid):
    size = len(grid)

    horizon = [(0, (0, 0))]
    horizon_set = set(horizon)
    remaining_nodes = set([(i, j) for i in range(size) for j in range(size)])

    cost_grid = [[float('inf') for _ in range(size)] for _ in range(size)]
    cost_grid[0][0] = 0

    while horizon:
        cost, (x, y) = heapq.heappop(horizon)
        remaining_nodes.remove((x, y))
        horizon_set.remove((cost, (x, y)))
        for x2, y2 in neighbors(x, y):
            if (x2, y2) not in remaining_nodes:
                continue
            added_cost = grid[x2][y2]
            cost_grid[x2][y2] = min(cost_grid[x2][y2], cost + added_cost)
            if (cost_grid[x2][y2], (x2, y2)) not in horizon_set:
                horizon_set.add((cost_grid[x2][y2], (x2, y2)))
                heapq.heappush(horizon, (cost_grid[x2][y2], (x2, y2)))

    return cost_grid[-1][-1]


grid_1 = [[int(c) for c in line] for line in data.splitlines()]
print("Part 1:", run(grid_1)) # 592


grid_2 = []
for i in range(5):
    for line in grid_1:
        new_line = []
        for j in range(5):
            for num in line:
                new_num = num + i + j
                if new_num > 9:
                    new_num %= 9
                new_line.append(new_num)
        grid_2.append(new_line)

print("Part 2:", run(grid_2)) # 2897

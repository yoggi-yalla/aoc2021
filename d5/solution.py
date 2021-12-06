import re

with open('input.txt') as f:
    data = f.read()

def parse_line(l):
    pattern = r"(\d*),(\d*) -> (\d*),(\d*)"
    x1, y1, x2, y2 = re.search(pattern, l).groups()
    return (int(x1), int(y1)), (int(x2), int(y2))

def count(grid):
    count = 0
    for i in range(1000):
        for j in range(1000):
            if grid[i][j] > 1:
                count += 1
    return count

grid_1 = [[0 for _ in range(1000)] for _ in range(1000)]
grid_2 = [[0 for _ in range(1000)] for _ in range(1000)]

lines = [parse_line(l) for l in data.splitlines()]
straight_lines = [l for l in lines if (l[0][0] == l[1][0]) or (l[0][1]) == l[1][1]]

def run(grid, lines):
    for (x1, y1), (x2, y2) in lines:
        dx = x2 - x1
        dy = y2 - y1
        steps = max(abs(dx), abs(dy))
        
        x_dir = int(dx / steps)
        y_dir = int(dy / steps)

        for i in range(steps + 1):
            grid[x1 + x_dir * i][y1 + y_dir * i] += 1
    return count(grid)

print("Part 1:", run(grid_1, straight_lines))
print("Part 2:", run(grid_2, lines))

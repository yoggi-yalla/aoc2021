with open('input.txt') as f:
    data = f.read()

grid = [[int(ch) for ch in line] for line in data.splitlines()]
height = len(grid)
width = len(grid[0])

directions = (
    (1,0),
    (-1,0),
    (0,1),
    (0,-1)
)

def is_inside(x, y):
    if x < height and y < width and x >= 0 and y >= 0:
        return True
    return False

def explore_basin(x, y, trail):
    if not is_inside(x,y):
        return

    if grid[x][y] == 9:
        return

    if (x, y) in trail:
        return

    trail.add((x, y))
    for dx, dy in directions:
        x2, y2 = x + dx, y + dy
        explore_basin(x2, y2, trail)
    return


count_1 = 0
low_points = []
for x in range(height):
    for y in range(width):
        for dx,dy in directions:
            x2 = x + dx
            y2 = y + dy
            if not is_inside(x2, y2):
                continue
            if grid[x2][y2] <= grid[x][y]:
                break
        else:
            low_points.append((x,y))
            count_1 += grid[x][y] + 1
print("Part 1:", count_1)


basins = []
for x, y in low_points:
    local_basin = set()
    explore_basin(x, y, local_basin)
    basins.append(local_basin)

basins.sort(key=lambda v: len(v), reverse=True)
count_2 = 1
for b in basins[:3]:
    count_2 *= len(b)
print("Part 2:", count_2)

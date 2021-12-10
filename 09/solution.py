with open('input.txt') as f:
    data = f.read()

grid = [[int(ch) for ch in line] for line in data.splitlines()]
height = len(grid)
width = len(grid[0])

directions = [(1,0), (-1,0), (0,1), (0,-1)]

def is_out_of_bounds(x, y):
    return x >= height or y >= width or x < 0 or y < 0

def explore_basin(x, y, local_basin):
    if (
        (x, y) in local_basin or
        is_out_of_bounds(x, y) or
        grid[x][y] == 9
    ):
        return local_basin

    local_basin.add((x, y))
    for dx, dy in directions:
        x2, y2 = x + dx, y + dy
        explore_basin(x2, y2, local_basin)
    return local_basin


count_1 = 0
low_points = []
for x in range(height):
    for y in range(width):
        for dx, dy in directions:
            x2, y2 = x + dx, y + dy
            if is_out_of_bounds(x2, y2):
                continue
            if grid[x2][y2] <= grid[x][y]:
                break
        else:
            low_points.append((x, y))
            count_1 += grid[x][y] + 1
print("Part 1:", count_1)

basin_sizes = []
for x, y in low_points:
    local_basin = explore_basin(x, y, set())
    basin_sizes.append(len(local_basin))

basin_sizes.sort(reverse=True)
print("Part 2:", basin_sizes[0] * basin_sizes[1] * basin_sizes[2])

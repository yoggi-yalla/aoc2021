with open('input.txt') as f:
    data = f.read()

groups = data.split('\n\n')

coords = []
for line in groups[0].splitlines():
    x, y = (int(c) for c in line.split(','))
    coords.append((x,y))

folds = []
for line in groups[1].splitlines():
    along = line.split(" ")[2]
    axis, value = along.split('=')
    folds.append((axis, int(value)))

max_x = max(folds, key=lambda v: (v[0] == 'x', v[1]))[1] * 2 + 1
max_y = max(folds, key=lambda v: (v[0] == 'y', v[1]))[1] * 2 + 1

grid = [["." for _ in range(max_x)] for _ in range(max_y)]
for x, y in coords:
    grid[y][x] = '#'


def show(grid):
    for line in grid:
        print("".join(line))

def fold(grid, axis):
    size_y = len(grid)
    size_x = len(grid[0])
    if axis == 'y':
        for i in range(size_y // 2):
            row = grid.pop()
            for j in range(size_x):
                if row[j] == '#':
                    grid[i][j] = '#'
        grid.pop()
    else:
        for i in range(size_y):
            for j in range(size_x // 2):
                v = grid[i].pop()
                if v == '#':
                    grid[i][j] = '#'
            grid[i].pop()

def count(grid):
    count = 0
    for i in range(len(grid)):
        for j in range(len(grid[0])):
            if grid[i][j] == '#':
                count += 1
    return count


for i, (axis, _) in enumerate(folds):
    fold(grid, axis)
    if i == 0:
        print("Part 1:", count(grid)) # 592

print("Part 2:")
show(grid) # JGAJEFKU

with open('input.txt') as f:
    data = f.read()

neighbors = [
    (-1, -1),
    (-1,  0),
    (-1,  1),
    ( 0, -1),
    ( 0,  0), 
    ( 0,  1),
    ( 1, -1),
    ( 1,  0),
    ( 1,  1)
]

def pad(grid):
    new_grid = []
    new_grid.append(['0' for _ in range(len(grid[0]) + 2)])
    for line in grid:
        new_grid.append(['0', *line, '0'])
    new_grid.append(['0' for _ in range(len(grid[0]) + 2)])
    return new_grid

def update(grid):
    new_grid = [[ch for ch in line] for line in grid]
    for x in range(1, len(grid) - 1):
        for y in range(1, len(grid[0]) - 1):
            b_num = ""
            for dx, dy in neighbors:
                x2, y2 = x + dx, y + dy
                b_num += grid[x2][y2]
            new_grid[x][y] = algorithm[int(b_num, base=2)]
    new_grid[0] = [new_grid[1][1] for _ in range(len(grid[0]))]
    for line in new_grid:
        line[0] = line[1]
        line[-1] = line[1]
    new_grid[-1] = [new_grid[1][1] for _ in range(len(grid[0]))]
    return new_grid

def expand(grid):
    new_grid = []
    continuation = grid[0][0]
    new_grid.append([continuation for _ in range(len(grid[0]) + 2)])
    for line in grid:
        new_grid.append([continuation, *line, continuation])
    new_grid.append([continuation for _ in range(len(grid[0]) + 2)])
    return new_grid

def count(grid):
    return sum(sum(int(i) for i in line) for line in grid)


data = data.replace('.', '0').replace('#', '1')

algorithm, image = data.split('\n\n')

grid = [[c for c in line] for line in image.splitlines()]
grid = pad(pad(pad(grid)))


for i in range(50):
    grid = update(grid)
    grid = expand(grid)
    if i == 1:
        print("Part 1:", count(grid))

print("Part 2:", count(grid))

with open('input.txt') as f:
    data = f.read()


grid = [[c for c in line] for line in data.splitlines()]

size_x = len(grid)
size_y = len(grid[0])

def get_east_buffer(grid):
    buffer = []
    for x in range(size_x):
        for y in range(size_y):
            if grid[x][y] == '>':
                if y == size_y - 1:
                    if grid[x][0] == '.':
                        buffer.append(((x, y), '.'))
                        buffer.append(((x, 0), '>'))
                else:
                    if grid[x][y+1] == '.':
                        buffer.append(((x, y), '.'))
                        buffer.append(((x, y + 1), '>'))
    return buffer

def get_south_buffer(grid):
    buffer = []
    for x in range(size_x):
        for y in range(size_y):
            if grid[x][y] == 'v':
                if x == size_x - 1:
                    if grid[0][y] == '.':
                        buffer.append(((x, y), '.'))
                        buffer.append(((0, y), 'v'))
                else:
                    if grid[x+1][y] == '.':
                        buffer.append(((x, y), '.'))
                        buffer.append(((x + 1, y), 'v'))
    return buffer

def update_grid(grid, buffer):
    for (x, y), v in buffer:
        grid[x][y] = v

def show(grid):
    for line in grid:
        print("".join(line))

iteration = 0
while True:
    iteration += 1
    east_buffer = get_east_buffer(grid)
    update_grid(grid, east_buffer)

    south_buffer = get_south_buffer(grid)
    update_grid(grid, south_buffer)

    if not east_buffer and not south_buffer:
        break


print("Part 1 & 2:", iteration) # 308

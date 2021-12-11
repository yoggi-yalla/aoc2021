with open('input.txt') as f:
    data = f.read()

grid = [[int(ch) for ch in line] for line in data.splitlines()]
size = len(grid)

directions = (
    (-1, -1),
    (-1,  0),
    (-1,  1),
    ( 0, -1),
    ( 0,  1),
    ( 1, -1),
    ( 1,  0),
    ( 1,  1)
)

def is_out_of_bounds(x, y):
    return x >= size or y >= size or x < 0 or y < 0

def add_1(grid):
    for x in range(size):
        for y in range(size):
            grid[x][y] += 1

def get_buffer(grid):
    buffer = []
    for x in range(size):
        for y in range(size):
            if grid[x][y] == 10:
                buffer.append((x, y))
    return buffer

def emit_light(grid, buffer):
    count = 0
    while buffer:
        x, y = buffer.pop()
        count += 1
        grid[x][y] = 0
        for dx, dy in directions:
            x2, y2 = x + dx, y + dy
            if is_out_of_bounds(x2, y2):
                continue
            if grid[x2][y2] != 0:
                grid[x2][y2] += 1
                if grid[x2][y2] == 10:
                    buffer.append((x2, y2))
    return count

iteration = 0
total_count = 0
while 1:
    add_1(grid)
    buffer = get_buffer(grid)
    current_count = emit_light(grid, buffer)
    total_count += current_count

    iteration += 1
    if iteration == 100:
        print("Part 1:", total_count) # 1640
    if current_count == 100:
        print("Part 2:", iteration) # 312
        break

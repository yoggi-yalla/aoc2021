import re

data = "target area: x=211..232, y=-124..-69"
pattern = r"target area: x=(-?\d*)..(-?\d*), y=(-?\d*)..(-?\d*)"

x_min, x_max, y_min, y_max = (int(x) for x in re.match(pattern, data).groups())


def valid_velocity(dx, dy):
    x, y = (0, 0)
    while True:
        x, y = x + dx, y + dy
        if x > x_max or y < y_min:
            return False
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return True
        dx, dy = max(dx - 1, 0), dy - 1


possible_dx = []
for i in range(x_max + 1):
    dx = i
    x_pos = 0
    while x_pos < x_max:
        x_pos += dx
        dx -= 1
        if dx < 0:
            break
        if x_min <= x_pos <= x_max:
            possible_dx.append(i)
            break

possible_dy = []
for i in range(y_min, -y_min + 1):
    dy = i
    y_pos = 0
    while y_pos > y_min:
        y_pos += dy
        dy -= 1
        if y_min <= y_pos <= y_max:
            possible_dy.append(i)
            break

valid_dx_dy = []
for dy in possible_dy[::-1]:
    for dx in possible_dx[::-1]:
        if valid_velocity(dx, dy):
            valid_dx_dy.append((dx, dy))


print("Part 1:", sum(range(valid_dx_dy[0][1] + 1)))
print("Part 2:", len(valid_dx_dy))

import re

data = "target area: x=211..232, y=-124..-69"
pattern = r"target area: x=(-?\d*)..(-?\d*), y=(-?\d*)..(-?\d*)"

x_min, x_max, y_min, y_max = (int(x) for x in re.match(pattern, data).groups())


def is_valid_velocity(dx, dy):
    x, y = (0, 0)
    while x <= x_max and y >= y_min:
        if x_min <= x <= x_max and y_min <= y <= y_max:
            return True
        x, y = x + dx, y + dy
        dx, dy = max(dx - 1, 0), dy - 1
    return False


valid_velocities = []
for dy in range(-y_min, y_min - 1, -1):
    for dx in range(x_max + 1):
        if is_valid_velocity(dx, dy):
            valid_velocities.append((dx, dy))

print("Part 1:", sum(range(valid_velocities[0][1] + 1))) # 7626
print("Part 2:", len(valid_velocities)) # 2032

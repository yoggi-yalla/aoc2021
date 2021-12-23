import re

with open("input.txt") as f:
    data = f.read()


PATTERN = r"(\w+) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)"

def parse_line(line):
    groups = re.search(PATTERN, line).groups()
    return tuple([groups[0] == "on", *(int(x) for x in groups[1:])])

instructions = [parse_line(line) for line in data.splitlines()]


def overlaps(box1, box2):
    x_min_1, x_max_1, y_min_1, y_max_1, z_min_1, z_max_1 = box1
    x_min_2, x_max_2, y_min_2, y_max_2, z_min_2, z_max_2 = box2
    return (
        x_max_1 >= x_min_2
        and x_max_2 >= x_min_1
        and y_max_1 >= y_min_2
        and y_max_2 >= y_min_1
        and z_max_1 >= z_min_2
        and z_max_2 >= z_min_1
    )

def get_left_remainder(new_box, existing_box):
    if new_box[0] <= existing_box[0]:
        return set()
    return {
        (
            existing_box[0],
            new_box[0] - 1,
            existing_box[2],
            existing_box[3],
            existing_box[4],
            existing_box[5],
        )
    }

def get_right_remainder(new_box, existing_box):
    if new_box[1] >= existing_box[1]:
        return set()
    return {
        (
            new_box[1] + 1,
            existing_box[1],
            existing_box[2],
            existing_box[3],
            existing_box[4],
            existing_box[5],
        )
    }

def get_front_remainder(new_box, existing_box):
    if new_box[2] <= existing_box[2]:
        return set()
    return {
        (
            max(new_box[0], existing_box[0]),
            min(new_box[1], existing_box[1]),
            existing_box[2],
            new_box[2] - 1,
            existing_box[4],
            existing_box[5],
        )
    }

def get_back_remainder(new_box, existing_box):
    if new_box[3] >= existing_box[3]:
        return set()
    return {
        (
            max(new_box[0], existing_box[0]),
            min(new_box[1], existing_box[1]),
            new_box[3] + 1,
            existing_box[3],
            existing_box[4],
            existing_box[5],
        )
    }

def get_bottom_remainder(new_box, existing_box):
    if new_box[4] <= existing_box[4]:
        return set()
    return {
        (
            max(new_box[0], existing_box[0]),
            min(new_box[1], existing_box[1]),
            max(new_box[2], existing_box[2]),
            min(new_box[3], existing_box[3]),
            existing_box[4],
            new_box[4] - 1,
        )
    }

def get_top_remainder(new_box, existing_box):
    if new_box[5] >= existing_box[5]:
        return set()
    return {
        (
            max(new_box[0], existing_box[0]),
            min(new_box[1], existing_box[1]),
            max(new_box[2], existing_box[2]),
            min(new_box[3], existing_box[3]),
            new_box[5] + 1,
            existing_box[5],
        )
    }

def count(on_cubes):
    count = 0
    for x_min, x_max, y_min, y_max, z_min, z_max in on_cubes:
        count += (x_max - x_min + 1) * (y_max - y_min + 1) * (z_max - z_min + 1)
    return count

def inside_initialization_area(box):
    return all(-50 <= box[i] <= 50 for i in range(6))


on_cubes = set()
initialization_running = True

for instruction in instructions:
    turn_on = instruction[0]
    new_box = instruction[1:]

    if initialization_running and not inside_initialization_area(new_box):
        initialization_running = False
        print("Part 1:", count(on_cubes))  # 612714

    removals = set()
    additions = set()

    if turn_on:
        additions.add(new_box)

    for box in on_cubes:
        if overlaps(new_box, box):
            removals.add(box)
            additions.update(get_left_remainder(new_box, box))
            additions.update(get_right_remainder(new_box, box))
            additions.update(get_front_remainder(new_box, box))
            additions.update(get_back_remainder(new_box, box))
            additions.update(get_bottom_remainder(new_box, box))
            additions.update(get_top_remainder(new_box, box))

    on_cubes.difference_update(removals)
    on_cubes.update(additions)

print("Part 2:", count(on_cubes))  # 1311612259117092

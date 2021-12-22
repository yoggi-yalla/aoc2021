import re
import itertools

with open('input.txt') as f:
    data = f.read()


pattern = r"(\w+) x=(-?\d+)..(-?\d+),y=(-?\d+)..(-?\d+),z=(-?\d+)..(-?\d+)"
def parse_line(line):
    groups = re.search(pattern, line).groups()
    return tuple([groups[0] == 'on', *(int(x) for x in groups[1:])])

instructions = [parse_line(line) for line in data.splitlines()]

def corners(box):
    x_min, x_max, y_min, y_max, z_min, z_max = box
    yield from itertools.product([x_min, x_max], [y_min, y_max], [z_min, z_max])

def is_inside(box, p):
    x_min, x_max, y_min, y_max, z_min, z_max = box
    return (
        x_min <= p[0] <= x_max and
        y_min <= p[1] <= y_max and
        z_min <= p[2] <= z_max 
    )

def overlaps(box1, box2):
    return any(
        is_inside(box1, p) for p in corners(box2)
    ) or any(
        is_inside(box2, p) for p in corners(box1)
    )


def get_left_remainder(new_box, existing_box):
    if new_box[0] <= existing_box[0]:
        return set()
    return set([(
        existing_box[0],
        new_box[0] - 1,
        existing_box[2],
        existing_box[3],
        existing_box[4],
        existing_box[5]
    )])

def get_right_remainder(new_box, existing_box):
    if new_box[1] >= existing_box[1]:
        return set()
    return set([(
        new_box[1] + 1,
        existing_box[1],
        existing_box[2],
        existing_box[3],
        existing_box[4],
        existing_box[5]
    )])

def get_front_remainder(new_box, existing_box):
    if new_box[2] <= existing_box[2]:
        return set()
    return set([(
        max(new_box[0], existing_box[0]),
        min(new_box[1], existing_box[1]),
        existing_box[2],
        new_box[2] - 1,
        existing_box[4],
        existing_box[5]
    )])

def get_back_remainder(new_box, existing_box):
    if new_box[3] >= existing_box[3]:
        return set()
    return set([(
        max(new_box[0], existing_box[0]),
        min(new_box[1], existing_box[1]),
        new_box[3] + 1,
        existing_box[3],
        existing_box[4],
        existing_box[5]
    )])

def get_bottom_remainder(new_box, existing_box):
    if new_box[4] <= existing_box[4]:
        return set()
    return set([(
        max(new_box[0], existing_box[0]),
        min(new_box[1], existing_box[1]),
        max(new_box[2], existing_box[2]),
        min(new_box[3], existing_box[3]),
        existing_box[4],
        new_box[4] - 1
    )])

def get_top_remainder(new_box, existing_box):
    if new_box[5] >= existing_box[5]:
        return set()
    return set([(
        max(new_box[0], existing_box[0]),
        min(new_box[1], existing_box[1]),
        max(new_box[2], existing_box[2]),
        min(new_box[3], existing_box[3]),
        new_box[5] + 1,
        existing_box[5]
    )])

def count(on_cubes):
    count = 0
    for x_min, x_max, y_min, y_max, z_min, z_max in on_cubes:
        count += (x_max - x_min + 1) * (y_max - y_min + 1) * (z_max - z_min + 1)
    return count

on_cubes = set()
for instruction in instructions:
    turn_on = instruction[0]
    new_box = instruction[1:]

    removals = set()
    additions = set()

    if turn_on:
        additions.add(new_box)

    for box in on_cubes:
        if overlaps(new_box, box):
            removals.add(box)
        else:
            continue
        
        additions.update(get_left_remainder(new_box, box))
        additions.update(get_right_remainder(new_box, box))
        additions.update(get_front_remainder(new_box, box))
        additions.update(get_back_remainder(new_box, box))
        additions.update(get_bottom_remainder(new_box, box))
        additions.update(get_top_remainder(new_box, box))
    
    on_cubes.difference_update(removals)
    on_cubes.update(additions)



print(count(on_cubes))

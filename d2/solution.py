with open('input.txt') as f:
    data = f.read()

def parse_line(l):
    dir, v = l.split(" ")
    return (dir, int(v))

instructions = [parse_line(l) for l in data.splitlines()]


h_pos = 0
v_pos = 0
for dir, v in instructions:
    if dir == 'down':
        v_pos += v
    if dir == 'up':
        v_pos -= v
    if dir == 'forward':
        h_pos += v
print("Part 1:", h_pos * v_pos)


h_pos = 0
v_pos = 0
aim = 0
for dir, v in instructions:
    if dir == 'down':
        aim += v
    if dir == 'up':
        aim -= v
    if dir == 'forward':
        h_pos += v
        v_pos += v * aim
print("Part 2:", h_pos * v_pos)

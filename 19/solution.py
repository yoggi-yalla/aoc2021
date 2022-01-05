with open('input.txt') as f:
    data = f.read()

def apply(func, array):
    for i, elem in enumerate(array):
        array[i] = func(elem)

def roll(v):
    return v[0], v[2], -v[1] 

def turn(v):
    return -v[1], v[0], v[2]

def rtr(v):
    return roll(turn(roll(v)))

class Scanner:
    def __init__(self):
        self.id = None
        self.observations = []

        self.dx = None
        self.dy = None
        self.dz = None

    @classmethod
    def from_string(cls, s):
        new = cls()
        lines = s.splitlines()
        new.id = int(lines[0].split(' ')[2])
        for line in lines[1:]:
            x, y, z = line.split(',')
            new.observations.append((int(x), int(y), int(z)))
        return new
    
    def orientations(self):
        for _ in range(2):
            for _ in range(3):
                apply(roll, self.observations)
                yield
                for _ in range(3):
                    apply(turn, self.observations)
                    yield
            apply(rtr, self.observations)


def overlaps(scanner, other):
    other_set = set(other.observations)
    for _ in scanner.orientations():
        for x1, y1, z1 in scanner.observations:
            for x2, y2, z2 in other.observations:
                dx, dy, dz = x2 - x1, y2 - y1, z2 - z1
                
                obs1_w_offset = [
                    (
                        obs[0] + dx,
                        obs[1] + dy,
                        obs[2] + dz
                    )
                    for obs in scanner.observations
                ]

                overlap = set.intersection(set(obs1_w_offset), other_set)

                if len(overlap) >= 12:
                    scanner.dx = dx + other.dx
                    scanner.dy = dy + other.dy
                    scanner.dz = dz + other.dz

                    return True
    return False


def get_size(scanners):
    max_distance = 0
    for s1 in scanners:
        for s2 in scanners:
            if s1 == s2:
                continue
            dst = abs(s1.dx - s2.dx) + abs(s1.dy - s2.dy) + abs(s1.dz - s2.dz)
            max_distance = max(max_distance, dst)
    return max_distance


def main():
    full_grid = {}

    scanners = [Scanner.from_string(s) for s in data.split('\n\n')]

    remaining_scanners = set(scanners)
    completed_scanners = set()

    first_scanner = scanners[0]
    for obs in first_scanner.observations:
        full_grid[obs] = 1

    first_scanner.dx = 0
    first_scanner.dy = 0
    first_scanner.dz = 0

    remaining_scanners.remove(first_scanner)
    completed_scanners.add(first_scanner)

    while remaining_scanners:
        for scanner in scanners:
            if scanner in completed_scanners:
                continue
            for other in completed_scanners:
                if overlaps(scanner, other):
                    for obs in scanner.observations:
                        obs_w_offset = obs[0] + scanner.dx, obs[1] + scanner.dy, obs[2] + scanner.dz
                        full_grid[obs_w_offset] = 1
                    remaining_scanners.remove(scanner)
                    completed_scanners.add(scanner)
                    break


    print("Part 1:", len(full_grid))
    print("Part 2:", get_size(scanners))

main()

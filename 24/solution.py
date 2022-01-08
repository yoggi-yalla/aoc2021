with open('input.txt') as f:
    data = f.read()

# Ended up solving this one by hand in "numbers" ... ¯\_(ツ)_/¯


def run(number):
    pointer = 0

    reg = {
        "w": 0,
        "x": 0,
        "y": 0,
        "z": 0
    }

    def reg_or_int(s):
        if s in reg:
            return reg[s]
        else:
            return int(s)

    for line in data.splitlines():
        split = line.split()

        op = split[0]
        a = split[1]
        if len(split) == 3:
            b = split[2]

        if op == 'inp':
            reg['w'] = int(str(number)[pointer])
            pointer += 1
        
        elif op == 'add':
            reg[a] += reg_or_int(b)

        elif op == 'mul':
            reg[a] *= reg_or_int(b)
        
        elif op == 'div':
            reg[a] //= reg_or_int(b)
        
        elif op == 'mod':
            reg[a] %= reg_or_int(b)
        
        elif op == 'eql':
            reg[a] = int(reg[a] == reg_or_int(b))

    return reg['z']


# Part 1:
assert run(92915979999498) == 0

# Part 2:
assert run(21611513911181) == 0


# Verification:
import random
def random_model_nbr_generator():
    while True:
        candidate = random.randint(int("1"*14), int("9"*14))
        if not "0" in str(candidate):
            yield candidate
rng = random_model_nbr_generator()

assert all(run(next(rng)) != 0 for _ in range(10000))

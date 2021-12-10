import itertools

with open('input.txt') as f:
    data = f.read()

def translate(string, mapping):
    return "".join([mapping[ch] for ch in string])

numbers = {
    frozenset("abcefg"):   "0",
    frozenset("cf"):       "1",
    frozenset("acdeg"):    "2",
    frozenset("acdfg"):    "3",
    frozenset("bcdf"):     "4",
    frozenset("abdfg"):    "5",
    frozenset("abdefg"):   "6",
    frozenset("acf"):      "7",
    frozenset("abcdefg"):  "8",
    frozenset("abcdfg"):   "9",
}


count_1 = 0
count_2 = 0
for line in data.splitlines():
    inputs = line.split("|")[0].split()
    outputs = line.split("|")[1].split()

    for digit in outputs:
        if len(digit) in (2, 3, 4, 7):
            count_1 += 1

    for c in itertools.permutations("abcdefg"):
        mapping = {f:t for f,t in zip("abcdefg", c)}

        for digit in inputs:
            if frozenset(translate(digit,mapping)) not in numbers:
                break
        else:
            count_2 += int("".join([numbers[frozenset(translate(d, mapping))] for d in outputs]))
            break

print("Part 1:", count_1) # 288
print("Part 2:", count_2) # 940724

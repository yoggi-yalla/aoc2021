from collections import Counter

with open('input.txt') as f:
    data = f.read()

groups = data.split('\n\n')
polymer_string = groups[0]
rules = {}
for line in groups[1].splitlines():
    f, t = line.split(' -> ')
    rules[tuple(f)] = t


letter_counts = Counter(polymer_string)
combination_counts = Counter()
for i in range(len(polymer_string) - 1):
    a, b = polymer_string[i], polymer_string[i + 1]
    combination_counts[(a, b)] += 1


for i in range(40):
    buffer = []
    for pair, count in combination_counts.items():
        new_letter = rules[pair]
        letter_counts[new_letter] += count
        combination_counts[pair] -= count
        buffer.append((pair, new_letter, count))

    for pair, new_letter, count in buffer:
        combination_counts[(pair[0], new_letter)] += count
        combination_counts[(new_letter, pair[1])] += count

    if i == 9:
        print("Part 1:", max(letter_counts.values()) - min(letter_counts.values()))

print("Part 2:", max(letter_counts.values()) - min(letter_counts.values()))

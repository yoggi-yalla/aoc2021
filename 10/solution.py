with open('input.txt') as f:
    data = f.read()

matching = {"(":")", "[":"]", "{":"}", "<":">"}
points_1 = {")":3, "]":57, "}":1197, ">":25137}
points_2 = {")":1, "]":2, "}":3, ">":4}

count_1 = 0
counts_2 = []
for line in data.splitlines():
    stack = []
    count_2 = 0
    for ch in line:
        if ch in ("(", "{", "[", "<"):
            stack.append(ch)
        else:
            if ch != matching.get(stack.pop()):
                count_1 += points_1[ch]
                break
    else:
        while stack:
            count_2 *= 5
            count_2 += points_2[matching[stack.pop()]]
        counts_2.append(count_2)

print("Part 1:", count_1)
print("Part 2:", sorted(counts_2)[len(counts_2) // 2])

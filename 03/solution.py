with open('input.txt') as f:
    data = f.read()

nums = [int(x, 2) for x in data.splitlines()]
digits = len(data.splitlines()[0])
length = len(data.splitlines())


def get_position_count(nums, pos):
    return len([n for n in nums if n & 1 << pos])

position_counts = {i:get_position_count(nums, i) for i in range(digits)}


gamma_rate = 0
epsilon_rate = 0
for pos, count in position_counts.items():
    if count >= length / 2:
        gamma_rate += 1 << pos
    else:
        epsilon_rate += 1 << pos

print("Part 1:", epsilon_rate * gamma_rate) # 2035764


sub_nums = nums.copy()
for pos in reversed(range(digits)):
    if len(sub_nums) == 1:
        break
    count = get_position_count(sub_nums, pos)
    if count >= len(sub_nums) / 2:
        sub_nums = [n for n in sub_nums if n & 1 << pos]
    else:
        sub_nums = [n for n in sub_nums if not n & 1 << pos]
og_rating = sub_nums.pop()


sub_nums = nums.copy()
for pos in reversed(range(digits)):
    if len(sub_nums) == 1:
        break
    count = get_position_count(sub_nums, pos)
    if count < len(sub_nums) / 2:
        sub_nums = [n for n in sub_nums if n & 1 << pos]
    else:
        sub_nums = [n for n in sub_nums if not n & 1 << pos]
co_rating = sub_nums.pop()

print("Part 2:", co_rating * og_rating) # 2817661
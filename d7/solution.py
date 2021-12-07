from functools import cache

with open('input.txt') as f:
    data = f.read()

@cache
def cached_sum_range(diff):
    return sum(range(1, diff + 1))


nums = [int(x) for x in data.split(',')]
left = min(nums)
right = max(nums)


costs_1 = []
costs_2 = []
for i in range(left, right):
    cost_1 = 0
    cost_2 = 0
    for num in nums:
        diff = abs(i - num)
        cost_1 += diff
        cost_2 += cached_sum_range(diff)
    costs_1.append(cost_1)
    costs_2.append(cost_2)
print("Part 1:", min(costs_1))
print("Part 2:", min(costs_2))

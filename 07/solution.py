with open('input.txt') as f:
    data = f.read()

nums = [int(x) for x in data.split(',')]

costs_1 = []
costs_2 = []
for i in range(min(nums), max(nums)):
    cost_1 = 0
    cost_2 = 0
    for num in nums:
        diff = abs(i - num)
        cost_1 += diff
        cost_2 += diff * (diff + 1) // 2
    costs_1.append(cost_1)
    costs_2.append(cost_2)
print("Part 1:", min(costs_1)) # 343605
print("Part 2:", min(costs_2)) # 96744904

with open('input.txt') as f:
    data = f.read()

nums = [int(x) for x in data.splitlines()]


count = 0
for i in range(len(nums) - 1):
    if nums[i+1] > nums[i]:
        count += 1
print("Part 1:", count)


count = 0
for i in range(len(nums) - 3):
    if nums[i + 3] > nums[i]:
        count += 1
print("Part 2:", count)

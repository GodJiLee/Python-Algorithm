# Input
nums = [-1, 0, 1, 2, -1, -4]

# 1.
import collections
sums = collections.defaultdict(list)
for i in range(len(nums)):
    for j in range(i+1, len(nums)):
        sums[nums[i]+nums[j]] = [nums[i], nums[j]]

res = []
for num in nums:
    if -num in sums.keys() and num not in sums.get(-num):
        res = sums.get(-num)
        res.append(num)

res

# 2.
# Input
nums = [-1, 0, 1, 2, -1, -4]

results = []
nums.sort()

# Brute force (n^3)
for i in range(len(nums) - 2):
    # continue to duplicate value
    if i > 0 and nums[i] == nums[i - 1]:
        continue
    for j in range(i + 1, len(nums) - 1):
        if j > i + 1 and nums[j] == nums[j - 1]:
            continue
        for k in range(j + 1, len(nums)):
            if k > j + 1 and nums[k] == nums[k - 1]:
                continue
            if nums[i] + nums[j] + nums[k] == 0:
                results.append((nums[i], nums[j], nums[k]))

    print(results)

# Two-Pointer

# Input
nums = [-1, 0, 1, 2, -1, -4]

results = []
nums.sort()

for i in range(len(nums) - 2):
    # continue to duplicate value
    if i > 0 and nums[i] == nums[i - 1]:
        continue

    # calculate sum
    left, right = i + 1, len(nums) - 1
    while left < right:
        sum = nums[i] + nums[left] + nums[right]
        if sum < 0:
            left += 1
        elif sum > 0 :
            right -= 1
        else:
            # sum = 0
            results.append((nums[i], nums[left], nums[right]))

            while left < right and nums[left] == nums[left + 1]:
                left += 1

            while left < right and nums[right] == nums[right - 1]:
                right -= 1

            left += 1
            right -= 1

print(results)
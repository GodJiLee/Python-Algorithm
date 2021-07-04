# Input
nums = [2, 7, 11, 15]
target = 9


# Brute Force
for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            print([i, j])


# Input
nums = [2, 7, 11, 15]
target = 9

# two-pointer
nums.sort()
right = len(nums)-1
res = 0
for left in nums:
    if left + nums[right] == target:
        res = nums.index(left)
        print(res)
    else:
        right -= 1

left, right = 0, len(nums)-1
while not left == right:
    # 합이 target보다 작으면 왼쪽 포인터를 오른 쪽으로
    if nums[left] + nums[right] < target:
        left += 1
    # 합이 target보다 크면 오른쪽 포인터를 왼쪽으로
    elif nums[left] + nums[right] > target:
        right -= 1
    else:
        print([left, right])

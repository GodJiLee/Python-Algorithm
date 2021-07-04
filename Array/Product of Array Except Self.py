nums = [1, 2, 3, 4]

# Two-Pointer
products = [1 for x in range(len(nums))]
for i in range(len(nums)):
    left, right = i - 1, i + 1

    while left >= 0:
        products[i] *= nums[left]
        if left > 0:
            left -= 1
        else:  
            break

    while right <= len(nums) - 1:
        products[i] *= nums[right]
        if right < len(nums) - 1:
            right += 1
        else:
            break

# 1.
out = []
p = 1
# left side product
for i in range(0, len(nums)):
    out.append(p)
    p = p * nums[i]
p = 1
# right side products
for i in range(len(nums) - 1, 0 - 1, -1):
    out[i] = out[i] * p
    p = p * nums[i]

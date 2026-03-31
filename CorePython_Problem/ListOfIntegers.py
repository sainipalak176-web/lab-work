# Input data
nums = [2, 4, 3, 5, 7, 8, 1]
target = 6

# Find pairs whose sum equals target
pairs = []

for i in range(len(nums)):
    for j in range(i + 1, len(nums)):
        if nums[i] + nums[j] == target:
            pairs.append((nums[i], nums[j]))

# Print result
print(pairs)
# Output: [(2, 4), (5, 1)]
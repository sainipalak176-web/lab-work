# Count frequency of elements in list

# Input
numbers = list(map(int, input().split()))
# Example input: 1 2 2 3 4 4 4 5

# Dictionary to store frequency
frequency = {}

for num in numbers:
    if num in frequency:
        frequency[num] += 1
    else:
        frequency[num] = 1

# Output
for key in frequency:
    print(key, ":", frequency[key])

# Example Output:
# 1 : 1
# 2 : 2
# 3 : 1
# 4 : 3
# 5 : 1
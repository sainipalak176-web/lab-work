# Check whether tuple elements are unique

# Input
values = tuple(map(int, input().split()))
# Example input: 1 2 3 4 5

# Check uniqueness
is_unique = True

for i in range(len(values)):
    for j in range(i + 1, len(values)):
        if values[i] == values[j]:
            is_unique = False
            break
    if not is_unique:
        break

# Output
if is_unique:
    print("Unique")
else:
    print("Not Unique")

# Example Output:
# Unique
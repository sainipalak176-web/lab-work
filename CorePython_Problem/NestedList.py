# Input data
nested_list = [1, [2, 3], [4, [5, 6]], 7]

# Function to flatten list (using recursion)
def flatten(lst):
    result = []
    for item in lst:
        if isinstance(item, list):
            result.extend(flatten(item))
        else:
            result.append(item)
    return result

# Get flattened list
flat_list = flatten(nested_list)

# Print result
print(flat_list)
# Output: [1, 2, 3, 4, 5, 6, 7]
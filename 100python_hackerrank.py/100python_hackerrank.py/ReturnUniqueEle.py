# Return unique elements from a list using function

# Function to get unique elements
def unique_elements(lst):
    unique_list = []
    for item in lst:
        if item not in unique_list:
            unique_list.append(item)
    return unique_list

# Input
numbers = list(map(int, input().split()))
# Example input: 1 2 2 3 4 4 5

# Output
print(unique_elements(numbers))
# Output: [1, 2, 3, 4, 5]
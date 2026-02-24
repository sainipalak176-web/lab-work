# Merge two dictionaries manually

# Input
n1 = int(input())   # Number of elements in first dictionary
dict1 = {}

for i in range(n1):
    key = input()
    value = int(input())
    dict1[key] = value

n2 = int(input())   # Number of elements in second dictionary
dict2 = {}

for i in range(n2):
    key = input()
    value = int(input())
    dict2[key] = value

# Merge dictionaries manually
merged_dict = {}

for key in dict1:
    merged_dict[key] = dict1[key]

for key in dict2:
    merged_dict[key] = dict2[key]

# Output
print(merged_dict)

# Example Output:
# {'A': 10, 'B': 20, 'C': 30}
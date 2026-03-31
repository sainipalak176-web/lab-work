import numpy as np

arr = np.arange(1, 26).reshape(5, 5)
sub_matrix = arr[1:4, 1:4]

print(sub_matrix)

# Output:
# [[ 7  8  9]
#  [12 13 14]
#  [17 18 19]]
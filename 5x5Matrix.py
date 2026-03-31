import numpy as np

matrix = np.random.randint(1, 101, (5, 5))
print("Matrix:")
print(matrix)

print("\nMin =", matrix.min())
print("Max =", matrix.max())

# Example Output:
# Matrix:
# [[23 45 12 89 34]
#  [67 11 90 54 32]
#  [76 28 19 47 65]
#  [14 73 52 39 81]
#  [60 21 48 70 16]]
#
# Min = 11
# Max = 90
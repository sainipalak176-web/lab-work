import numpy as np

# Input: 2D NumPy array
matrix = np.array([[1, 2, 3],
                   [4, 5, 6],
                   [7, 8, 9]])

# Extract diagonal elements
diagonal = np.diag(matrix)

# Output
print("Diagonal Elements:", diagonal)
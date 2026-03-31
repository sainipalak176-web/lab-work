# Input data
students = [("Aman", 85), ("Riya", 92), ("Sohan", 78), ("Neha", 88)]

# Sorting based on marks (second element of tuple)
sorted_students = sorted(students, key=lambda x: x[1])

# Print result
print(sorted_students)
# Output: [('Sohan', 78), ('Aman', 85), ('Neha', 88), ('Riya', 92)]
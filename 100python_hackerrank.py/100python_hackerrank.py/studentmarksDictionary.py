# Create student marks dictionary and find topper

# Input
n = int(input())   # Number of students

students = {}

# Read student name and marks
for i in range(n):
    name = input()
    marks = int(input())
    students[name] = marks

# Find topper
topper = ""
highest_marks = -1

for name in students:
    if students[name] > highest_marks:
        highest_marks = students[name]
        topper = name

# Output
print(topper, highest_marks)

# Example Output:
# Rahul 95
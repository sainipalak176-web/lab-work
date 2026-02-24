# Find maximum of three numbers using function

# Function to find maximum
def find_max(a, b, c):
    if a >= b and a >= c:
        return a
    elif b >= a and b >= c:
        return b
    else:
        return c

# Input
x = int(input())    # Example input: 10
y = int(input())    # Example input: 25
z = int(input())    # Example input: 15

# Output
print(find_max(x, y, z))   # Output: 25
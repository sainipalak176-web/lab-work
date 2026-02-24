# Find sum of digits using function

# Function to calculate sum of digits
def sum_of_digits(n):
    total = 0
    for digit in str(n):
        total += int(digit)
    return total

# Input
num = int(input())     # Example input: 1234

# Output
print(sum_of_digits(num))   # Output: 10
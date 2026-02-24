# Find factorial using function

# Function to calculate factorial
def factorial(n):
    fact = 1
    for i in range(1, n + 1):
        fact *= i
    return fact

# Input
num = int(input())     # Example input: 5

# Output
print(factorial(num))  # Output: 120
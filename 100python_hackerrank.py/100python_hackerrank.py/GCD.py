# Find GCD using function

# Function to calculate GCD
def find_gcd(a, b):
    while b != 0:
        a, b = b, a % b
    return a

# Input
num1 = int(input())     # Example input: 12
num2 = int(input())     # Example input: 18

# Output
print(find_gcd(num1, num2))   # Output: 6
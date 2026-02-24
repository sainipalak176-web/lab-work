# Check prime number using function

# Function to check prime
def is_prime(n):
    if n <= 1:
        return False
    for i in range(2, n):
        if n % i == 0:
            return False
    return True

# Input
num = int(input())     # Example input: 7

# Output
if is_prime(num):
    print("Prime Number")
else:
    print("Not a Prime Number")

# Output (for input 7):
# Prime Number
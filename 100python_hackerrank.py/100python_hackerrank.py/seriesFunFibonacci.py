# Generate Fibonacci series using function

# Function to generate Fibonacci series
def fibonacci(n):
    a = 0
    b = 1
    for i in range(n):
        print(a, end=" ")
        c = a + b
        a = b
        b = c

# Input
num = int(input())      # Example input: 7

# Output
fibonacci(num)          # Output: 0 1 1 2 3 5 8
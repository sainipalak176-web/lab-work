# Print multiplication tables from 1 to 10

# No input required (standard tables 1 to 10)

for i in range(1, 11):          # Tables from 1 to 10
    for j in range(1, 11):      # Multiplication up to 10
        print(i, "x", j, "=", i * j)
    print()   # Empty line after each table
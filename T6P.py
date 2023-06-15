# Old way
if len(data) > 0:
    count = len(data)
    print(f"There are {count} items.")

# New way with the walrus operator
if (count := len(data)) > 0:
    print(f"There are {count} items.")

# Calculate the sum of even numbers in a list
numbers = [1, 2, 3, 4, 5, 6, 7, 8, 9, 10]
even_sum = sum(num for num in numbers if (num % 2 == 0))

print(f"The sum of even numbers is: {even_sum}")
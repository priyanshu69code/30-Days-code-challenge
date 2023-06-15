import functools

def multiply(a, b):
    return a * b

double = functools.partial(multiply, b=2)
result = double(5)  # Output: 10

from functools import reduce

numbers = [1, 2, 3, 4, 5]
product = reduce(lambda x, y: x * y, numbers)
# Output: 120 (1 * 2 * 3 * 4 * 5)
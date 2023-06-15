#  Permutations and Combinations
import itertools

numbers = [1, 2, 3]
permutations = list(itertools.permutations(numbers, 2))
combinations = list(itertools.combinations(numbers, 2))

print(permutations)  # [(1, 2), (1, 3), (2, 1), (2, 3), (3, 1), (3, 2)]
print(combinations)  # [(1, 2), (1, 3), (2, 3)]

# Infinite Iterators

counter = itertools.count(start=1, step=2)
repeated_values = itertools.cycle(['A', 'B', 'C'])

for _ in range(5):
    print(next(counter))  # 1, 3, 5, 7, 9

for _ in range(5):
    print(next(repeated_values))  # A, B, C, A, B

# Advanced Filtering
import itertools

numbers = [1, 2, 3, 4, 5]
even_numbers = list(itertools.filterfalse(lambda x: x % 2 != 0, numbers))

print(even_numbers)  # [2, 4]


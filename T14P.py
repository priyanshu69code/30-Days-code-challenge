from collections import deque

my_queue = deque()
my_queue.append(1)
my_queue.append(2)
my_queue.append(3)

print(my_queue.popleft())  # Output: 1
print(my_queue)  # Output: deque([2, 3])

from collections import OrderedDict

my_dict = OrderedDict()
my_dict['a'] = 1
my_dict['b'] = 2
my_dict['c'] = 3

for key, value in my_dict.items():
    print(key, value)

# Output:
# a 1
# b 2
# c 3

from collections import ChainMap

dict1 = {'a': 1, 'b': 2}
dict2 = {'b': 3, 'c': 4}

combined_dict = ChainMap(dict1, dict2)

print(combined_dict['a'])  # Output: 1
print(combined_dict['b'])  # Output: 2 (from dict1)
print(combined_dict['c'])  # Output: 4 (from dict2)

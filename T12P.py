from collections import namedtuple

# Define a named tuple 'Person' with fields: name, age, and profession
Person = namedtuple('Person', ['name', 'age', 'profession'])

# Create a new person object
person1 = Person('John Doe', 30, 'Engineer')

# Access fields using dot notation
print(person1.name)  # Output: John Doe
print(person1.age)  # Output: 30
print(person1.profession)  # Output: Engineer



from collections import defaultdict

# Create a defaultdict with a default value of 0
word_count = defaultdict(int)

# Update the count of each word
words = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
for word in words:
    word_count[word] += 1

# Print the word count
print(word_count)  # Output: defaultdict(<class 'int'>, {'apple': 3, 'banana': 2, 'cherry': 1})



from collections import Counter

# Create a counter for a list of fruits
fruits = ['apple', 'banana', 'apple', 'cherry', 'banana', 'apple']
fruit_counter = Counter(fruits)

# Print the most common fruits
print(fruit_counter.most_common(2))  # Output: [('apple', 3), ('banana', 2)]

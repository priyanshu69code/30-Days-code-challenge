class MyList:
    def __init__(self):
        self.data = []

    def __len__(self):
        return len(self.data)

my_list = MyList()
my_list.data = [1, 2, 3, 4, 5]
print(len(my_list))  # Output: 5

class MyDict:
    def __init__(self):
        self.data = {}

    def __getitem__(self, key):
        return self.data.get(key, None)

my_dict = MyDict()
my_dict.data = {'name': 'John', 'age': 25}
print(my_dict['name'])  # Output: 'John'
print(my_dict['city'])  # Output: None

class MyList:
    def __init__(self):
        self.data = []

    def __setitem__(self, index, value):
        self.data[index] = value

my_list = MyList()
my_list.data = [1, 2, 3, 4, 5]
my_list[2] = 10
print(my_list.data)  # Output: [1, 2, 10, 4, 5]
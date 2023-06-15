numbers = [1, 2, 3, 4, 5]
squared_numbers = (x ** 2 for x in numbers)


def fibonacci():
    a, b = 0, 1
    while True:
        yield a
        a, b = b, a + b
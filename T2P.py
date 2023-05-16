def count_element_occurrences(element, tuple):
    count = 0
    for item in tuple:
        if item == element:
            count += 1
    return count

my_tuple = (1, 2, 3, 2, 4, 2, 5)
element_to_count = 2

result = count_element_occurrences(element_to_count, my_tuple)
print(f"The element {element_to_count} appears {result} times in the tuple.")
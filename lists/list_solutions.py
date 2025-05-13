
# Easy -1

def filter_even_numbers(numbers):
    return [x for x in numbers if x % 2 == 0]
print(filter_even_numbers([1,2,3,4,5,6]))
print(filter_even_numbers([1,3,5]))

# Easy - 2

def merge_sorted_lists(list1, list2):
    return sorted(list1 + list2)
print(merge_sorted_lists([1,3,5],[2,4,6]))
print(merge_sorted_lists([1,2,3],[4,5,6]))

# Medium - 1

def generate_matrix(n,m):
    return [[i * j for j in range(m)] for i in range(n)]
print(generate_matrix(3,3))

# Medium - 2

def transpose_matrix(matrix):
    return [list(row) for row in zip(*matrix)]
matrix = [
    [1,2,3],
    [4,5,6]
]
print(transpose_matrix(matrix))
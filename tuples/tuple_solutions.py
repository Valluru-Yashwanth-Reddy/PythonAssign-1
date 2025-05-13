# Easy - 1

def swap_pairs(tpl):
    lst = list(tpl)
    for i in range(0, len(lst)-1, 2):
        lst[i], lst[i+1] = lst[i+1], lst[i]
    return tuple(lst)
print(swap_pairs((1,2,3,4)))
print(swap_pairs((1,2,3)))

# Easy - 2

def get_stats(numbers):
    total = sum(numbers)
    return (min(numbers), max(numbers), total, total / len(numbers))
print(get_stats([1,2,3,4,5]))


# Medium - 1

from collections import namedtuple

Student = namedtuple("Student", ["name", "age", "grades"])
def top_student(students):
    return max(students, key=lambda student: sum(student.grades) / len(student.grades))

alice = Student("Alice", 20, (85, 90, 95))
bob = Student("Bob", 19, (70, 80, 90))
charlie = Student("Charlie", 21, (90, 92, 93))

print(top_student([alice, bob, charlie]))


# Medium - 2 
from collections import Counter
def count_coordinate_occurrences(coords):
    return dict(Counter(coords))
coords = [(1, 2), (3, 4), (1, 2), (5, 6), (3, 4), (1, 2)]
print(count_coordinate_occurrences(coords))
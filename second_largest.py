# please write a function that finds and returns
# the second largest element in a list of integers
import sys


def second_largest(lst):
    b2, b1 = sorted([lst[0], lst[1]])
    for l in lst[2:]:
        if l > b2 and l < b1:
            b2 = l
        if l >= b1:
            b2 = b1
            b1 = l
    return b2


print(second_largest([3, 5, 6, 1, 2]))

print(second_largest([4, 7, 8, 0, 5]))
print(second_largest([2, 6, 4, 1, 1]))

# this one is open
print(second_largest([0, 0, 1, 1]))
print(second_largest([1, 1, 0, 0]))

# this one is open too
print(second_largest([5, 4, 3, 2, 1]))

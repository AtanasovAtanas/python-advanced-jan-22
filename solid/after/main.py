from copy import copy

arr = [1, 2, 3]
arr2 = copy(arr)
arr2.append(4)

print(arr)
print(arr2)


def copy(arr):
    result = []
    for el in arr:
        result.append(el)
    return result

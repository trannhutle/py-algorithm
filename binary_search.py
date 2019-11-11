data = [2, 4, 5, 7, 8, 9, 14, 17, 22, 25, 27, 28, 33, 37]
target = 5


# Linear search
def linear_search(data, target):
    for i in range(len(data)):
        if data[i] == target:
            return True
    return False


def binary_search_iterative(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            # ignore element greater than the value that we are looking for
            high = mid - 1
        else:
            low = mid + 1
    return False


def binary_search_recursive(data, target, low, high):
    print(data, target, low, high)
    if low > high:
        return False
    else:
        mid = (low + high) // 2
        if target == data[mid]:
            return True
        elif target < data[mid]:
            return binary_search_recursive(data, target, low, mid - 1)
        else:
            return binary_search_recursive(data, target, mid + 1, high)


print(binary_search_iterative(data, target))
print(binary_search_recursive(data, target, 0, len(data) - 1))

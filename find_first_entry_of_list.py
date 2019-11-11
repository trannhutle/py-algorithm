def find_first_entry_of_list(data, target):
    low = 0
    high = len(data) - 1

    while low <= high:
        mid = (low + high) // 2

        if data[mid] < target:
            low = mid + 1
        elif data[mid] > target:
            high = mid - 1
        else:
            if mid - 1 < 0:
                return mid
            # Get the first dupplicated index
            if data[mid - 1] != target:
                return mid
            # Move to the left since we need to find the first dupplicated entry
            high = mid - 1


array = [-14, -10, 2, 108, 108, 243, 285, 285, 285, 401]
target = 108

print(find_first_entry_of_list(array, target))

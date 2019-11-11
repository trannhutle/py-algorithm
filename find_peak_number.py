def find_highest_number(data):
    low = 0
    high = len(data) - 1

    if len(data) < 3:
        return None

    while low <= high:
        mid = (low + high) // 2
        mid_left = data[mid - 1] if mid - 1 > 0 else float("-inf")
        mid_right = data[mid + 1] if mid + 1 > 0 else float("inf")

        # Move mid-point to right
        if mid_left < data[mid] and mid_right > data[mid]:
            low = mid + 1
        # Move mid-point to left
        elif mid_left > data[mid] and mid_right < data[mid]:
            high = mid - 1

        elif mid_left < data[mid] and mid_right < data[mid]:
            return data[mid]


# array = [1, 2, 3, 4, 5, 4, 3, 2, 1]
array = [1, 2, 3, 4, 1]
# array = [1, 6, 5, 4, 3, 2, 1]

x = find_highest_number(array)
print(x)
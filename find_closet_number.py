"""
Given an array of sorted integers. We need to find the closest value to the given number

Array may contain duplicate value and negative numbers
Examples:
    Input: arr[] = {1,2,4,5,6,6,8,90}
    Target nuymber = 11

    Output: 9

    9 is closet to 11 in given array
    Input: arr[] = {2,5,6,7,8,8,9}
    Target number = 4
    Output = 5
"""


def find_closet_num(data, target):
    min_diff = float("inf")
    low = 0
    high = len(data) - 1
    closest_num = None
    if len(data) == 0:
        return None
    if len(data) == 1:
        return data[0]

    while low < high:
        mid = (low + high) // 2
        # Ensure we do not read beyond the bound of the list
        # And obtain the lefdt and right difference values
        if mid + 1 < len(data):
            min_diff_right = abs(data[mid + 1] - target)
            print("min right {}".format(min_diff_right))
        if mid > 0:
            min_diff_left = abs(data[mid - 1] - target)
            print("min left {}".format(min_diff_left))

        # Check if the absolute value between left and right
        # elements are smaller than any seen prior
        if min_diff_left < min_diff:
            min_diff = min_diff_left
            closest_num = data[mid - 1]

        if min_diff_right < min_diff:
            min_diff = min_diff_right
            closest_num = data[mid + 1]

        print("closest number {}".format(closest_num))
        print("data[mid]  {}".format(data[mid]))

        # Use binary search to move mid-point
        # If the target is on the right hand side of the mid point (greater)
        if data[mid] < target:
            low = mid + 1
        # If the target is on the left hand side of the mid point (greater)
        elif data[mid] > target:
            high = mid - 1
        # If the target is equal to to mid-point, in this case the closest number is the mid-point
        else:
            print("this is ekse")
            return data[mid]

    return closest_num


data = [1, 2, 4, 5, 6, 6, 8, 9]
# data = [2, 5, 6, 7, 8, 8, 9]

print(find_closet_num(data, 11))

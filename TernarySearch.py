def ternarySearch(target, nums, left, right):
    if left > right:
        return -1  # Target not found

    third = (right - left) // 3
    mid1 = left + third
    mid2 = right - third

    if nums[mid1] == target:
        return mid1
    if nums[mid2] == target:
        return mid2

    if target > nums[mid1]:  # Target is in the left segment
        return ternarySearch(target, nums, left, mid1 - 1)
    elif target < nums[mid2]:  # Target is in the right segment
        return ternarySearch(target, nums, mid2 + 1, right)
    else:  # Target is in the middle segment
        return ternarySearch(target, nums, mid1 + 1, mid2 - 1)


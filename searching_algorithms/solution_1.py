"""
PROBLEM: Given a sorted array of integers and a target value,
return the index if found. Otherwise return -1.
"""

def search(nums, target):
    left, right = 0, len(nums)- 1

    while left <= right:
        mid = (left + right) // 2
        if nums[mid] == target:
            return mid
        elif nums[mid] < target:
            left = mid + 1
        else:
            right = mid - 1

    return - 1
"""
PROBLEM: Write a program that takes as input a permutation, and returns the next permutation under
dictionary ordering. if the permutation is the last permutation, return the empty array. for example,
if the input is (1,0,3,2) your function should return (1,2,0,3). if the input is (3,2,1,0), return ().

"""

# permutation is reordering of elements.
# lexicographic ordering is the ordering of elements in a dictionary.

# the LOGICAL APPROACH:
# first we scan from right to left to find the first place where
# a[i] < a[i+1]
# from the right side, we find the smallest number greater than a[i]
# we swap the two numbers
# then reverse everything to the right of i
# if the first step fails we return an empty array.

class Solution:
    def nextPermutation(self, nums):
        """
        Modify nums in-place to the next permutation.
        If nums is the last permutation, clear the list.
        """

        n = len(nums)

        # firstly, we look for the pivot index i, where nums[i] < nums[i+1]
        pivot = -1
        for i in range(n-2, -1, -1):
            if nums[i] < nums[i + 1]:
                pivot = i
                break

        # if no pivot is found, the list is already the last permutation
        if pivot == -1:
            nums.clear()
            return

        # find the smallest number greater than nums[pivot] to the right of pivot
        for j in range(n-1, pivot, -1):
            if nums[j] > nums[pivot]:
                nums[pivot], nums[j] = nums[j], nums[pivot]
                break
        
        # then reverse the suffix
        nums[pivot + 1:] = reversed(nums[pivot + 1:])
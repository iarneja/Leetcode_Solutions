# Maximum Subarray
# Given an integer array nums, find the contiguous subarray (containing at least one number) which has the largest sum and return its sum.
# A subarray is a contiguous part of an array.
# Time complexity : O(n)
# Space complexity : O(1)
def maxSubArray(nums):
    max_sum = float('-inf')
    current_sum = 0
    for n in nums:
        current_sum = max(n, current_sum + n)
        max_sum = max(max_sum, current_sum)
    return max_sum
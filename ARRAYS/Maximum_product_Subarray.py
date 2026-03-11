# Maximum Product Subarray
# Given an integer array nums, find a contiguous non-empty subarray within the array that has the largest product, and return the product.
# The test cases are generated so that the answer will fit in a 32-bit integer.
# Time complexity : O(n)
# Space complexity : O(1)   

from typing import List

class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        current_max = nums[0]
        current_min = nums[0]
        result = nums[0]

        for i in range(1, len(nums)):
            x = nums[i]
            temp_max = max(x, x*current_max, current_min)
            temp_min = min(x, x*current_max, current_min)
            
            current_max = temp_max
            current_min = temp_min
            result = max(result, current_max)

        return result
        
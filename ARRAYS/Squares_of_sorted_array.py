# 896 SQUARES OF SORTED ARRAY 


# BRUTE FORCE METHOD : 

# Time complexity : O(nlogn) 
# Space complexity : O(1) 

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        res = [0] * n
        for i in range(n):
            res[i] = nums[i] ** 2
        res.sort()
        return res


# TWO POINTERS METHOD :

# Time complexity : O(n) 
# Space complexity : O(1) 

from typing import List

class Solution:
    def sortedSquares(self, nums: List[int]) -> List[int]:
        n = len(nums)
        i, j = 0, n - 1
        res = [0] * n

        for k in range(n - 1, -1, -1):
            if nums[i] * nums[i] > nums[j] * nums[j]:
                res[k] = nums[i] * nums[i]
                i += 1
            else:
                res[k] = nums[j] * nums[j]
                j -= 1

        return res




# 896 MONOTONIC ARRAY 
# Time complexity : O(n) 
# Space complexity : O(1) 

# Solving it in easy way : 

from typing import List

class Solution:
    def isMonotonic(self, array: List[int]) -> bool:
        n = len(array)
        first = array[0]
        last = array[n - 1]

        if first > last:
            for k in range(n - 1):
                if array[k] < array[k + 1]:
                    return False

        elif first == last:
            for k in range(n - 1):
                if array[k] != array[k + 1]:
                    return False

        else:
            for k in range(n - 1):
                if array[k] > array[k + 1]:
                    return False

        return True


# Another way to solve it :

from typing import List

class Solution:
    def isMonotonic(self, nums: List[int]) -> bool:
        seen_up = False
        seen_down = False

        for i in range(len(nums) - 1):
            if nums[i] < nums[i + 1]:
                seen_up = True
            elif nums[i] > nums[i + 1]:
                seen_down = True

            if seen_up and seen_down:
                return False

        return True




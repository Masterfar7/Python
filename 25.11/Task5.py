"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-the-power-of-k-size-subarrays-i/description/
"""


from typing import List


class Solution:
    def resultsArray(self, nums: List[int], k: int) -> List[int]:
        l, r = 0, k - 1
        res = []

        def is_sorted(subarray: List[int]) -> int:
            for i in range(len(subarray) - 1):
                if subarray[i] + 1 != subarray[i + 1]:
                    return -1
            return subarray[-1]

        while r < len(nums):
            res.append(is_sorted(nums[l : r + 1]))
            l += 1
            r += 1

        return res


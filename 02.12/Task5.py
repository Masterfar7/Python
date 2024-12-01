"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/description/
"""


from typing import List


class Solution:
    def minOperations(nums: List[int]) -> int:
        n = len(nums)
        op = 0
        i = 0

        while i <= n - 3:
            if nums[i] == 0:
                # Flip 3 elements starting at index i
                for j in range(3):
                    nums[i + j] ^= 1
                op += 1
            i += 1

        if any(num == 0 for num in nums):
            return -1

        return op


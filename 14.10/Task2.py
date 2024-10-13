"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/target-sum/
"""

from typing import List

class Solution:
    def findTargetSumWays(self, nums: List[int], tar: int) -> int:
        a = {}

        def dfs(ind: int, total: int) -> int:
            if ind == len(nums):
                return 1 if total == tar else 0

            if (ind, total) in a:
                return a[(ind, total)]

            p = dfs(ind + 1, total + nums[ind])
            n = dfs(ind + 1, total - nums[ind])

            a[(ind, total)] = p + n

            return a[(ind, total)]

        return dfs(0, 0)

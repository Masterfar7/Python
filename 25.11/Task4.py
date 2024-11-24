"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/find-the-longest-equal-subarray/description/
"""


from typing import List


class Solution:
    def longestEqualSubarray(self, nums: List[int], k: int) -> int:
        mx = 0
        l = 0
        n = len(nums)
        dp = [0] * (n + 1)

        for r in range(n):
            dp[nums[r]] += 1
            mx = max(mx, dp[nums[r]])

            if (mx + k <= r - l):
                dp[nums[l]] -= 1
                l += 1

        return mx


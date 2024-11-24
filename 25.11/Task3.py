"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-nice-subarray/description/
"""


from typing import List


class Solution:
    def longestNiceSubarray(self, nums: List[int]) -> int:
        res, n, l = 1, len(nums), 0
        for r in range(1, n):
            t = r - 1
            while nums[r] & nums[t] == 0 and t >= l:
                t -= 1

            if (t == l - 1):
                res = max(res, r - l + 1)

            l = t + 1

        return res



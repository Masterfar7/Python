"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/length-of-longest-subarray-with-at-most-k-frequency/description/
"""


from collections import Counter
from typing import List


class Solution(object):
    def maxSubarrayLength(nums: List[int], k: int) -> int:
        l = 0
        mx = 0
        f = Counter()

        for right in range(len(nums)):
            f[nums[right]] += 1

            while f[nums[right]] > k:
                f[nums[l]] -= 1
                if f[nums[l]] == 0:
                    del f[nums[l]]
                l += 1

            mx = max(mx, right - l + 1)

        return mx

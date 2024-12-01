"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/maximum-sum-of-almost-unique-subarray/description/
"""


from collections import Counter
from typing import List


class Solution(object):
    def maxSum(self, nums, m, k):
        n = len(nums)
        if k > n:
            return 0

        l = 0
        sum = 0
        mx = 0
        f = Counter()

        for right in range(n):
            f[nums[right]] += 1
            sum += nums[right]

            if right - l + 1 > k:
                f[nums[l]] -= 1
                if f[nums[l]] == 0:
                    del f[nums[l]]
                sum -= nums[l]
                l += 1

            if right - l + 1 == k and len(f) >= m:
                mx = max(mx, sum)

        return mx



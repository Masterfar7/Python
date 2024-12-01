"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/continuous-subarrays/description/
"""


from typing import List


class Solution(object):
    def continuousSubarrays(nums: List[int]) -> int:
        l = 0
        sum = 0
        mn, mx = nums[0], nums[0]

        for right in range(len(nums)):
            mn = min(mn, nums[right])
            mx = max(mx, nums[right])

            while mx - mn > 2:
                l += 1
                mn = min(nums[l:right + 1])
                mx = max(nums[l:right + 1])

            sum += right - l + 1

            return sum
"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/maximum-erasure-value/description/
"""


from typing import List


class Solution:
    def maximumUniqueSubarray(self, nums: List[int]) -> int:
        mx = -9999
        mz = 0
        s = set()
        j = 0
        i = 0
        while j < len(nums):
            mz += nums[j]
            while nums[j] in s:
                mz -= nums[i]
                s.remove(nums[i])
                i += 1
            s.add(nums[j])
            if mx < mz:
                mx = mz
            j += 1
        return mx

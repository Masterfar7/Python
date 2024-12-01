"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/count-the-number-of-good-subarrays/description/
"""


from collections import Counter
from typing import List


class Solution(object):
    def countGood(nums: List[int], k: int) -> int:
        l = 0
        k = 0
        pk = 0
        fr = Counter()

        for right in range(len(nums)):
            fr[nums[right]] += 1
            pk += fr[nums[right]] - 1

            while pk >= k:
                k += len(nums) - right
                fr[nums[l]] -= 1
                pk -= fr[nums[l]]
                l += 1

        return k

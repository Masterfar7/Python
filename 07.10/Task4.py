"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/majority-element-ii/
"""

from typing import List


class Solution(object):
    def majorityElement(self, nums: List[int]) -> List[int]:
        if not nums:
            return []

        c1, c2, k1, k2 = None, None, 0, 0

        for num in nums:
            if c1 is not None and num == c1:
                k1 += 1
            elif c2 is not None and num == c2:
                k2 += 1
            elif k1 == 0:
                c1, k1 = num, 1
            elif k2 == 0:
                c2, k2 = num, 1
            else:
                k1 -= 1
                k2 -= 1

        k1, k2 = 0, 0

        for num in nums:
            if num == c1:
                k1 += 1
            elif num == c2:
                k2 += 1

        res = []
        n = len(nums)

        if k1 > n // 3:
            res.append(c1)
        if k2 > n // 3:
            res.append(c2)

        return res


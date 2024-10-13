"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/4sum-ii/
"""

from typing import List


class Solution:
    def fourSumCount(self, nums1: List[int], nums2: List[int], nums3: List[int], nums4: List[int]) -> int:
        count_map = {}

        for num1 in nums1:
            for num2 in nums2:
                sm = num1 + num2
                if sm in count_map:
                    count_map[sm] += 1
                else:
                    count_map[sm] = 1

        res = 0
        for num3 in nums3:
            for num4 in nums4:
                target = -(num3 + num4)
                if target in count_map:
                    res += count_map[target]

        return res


"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/binary-subarrays-with-sum/description/
"""


from collections import defaultdict
from typing import List


class Solution:
    def numSubarraysWithSum(self,nums: List[int], goal: int) -> int:
        pref = 0
        count = 0
        k = defaultdict(int)

        k[0] = 1

        for num in nums:
            pref += num

            if pref - goal in k:
                count += k[pref - goal]

            k[pref] += 1

        return count



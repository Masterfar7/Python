"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/number-of-boomerangs/
"""


from collections import defaultdict
from typing import List

class Solution:
    def numberOfBoomerangs(self, points: List[List[int]]) -> int:
        k = 0

        for p in points:
            dm = defaultdict(int)

            for q in points:
                if p != q:
                    dx = p[0] - q[0]
                    dy = p[1] - q[1]
                    dist = dx * dx + dy * dy
                    dm[dist] += 1

            for k in dm.values():
                k += k * (k - 1)

        return k

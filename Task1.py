"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/non-overlapping-intervals/
"""


from typing import List

class Solution:
    def eraseOverlapIntervals(self, intervals: List[List[int]]) -> int:
        if not intervals:
            return 0

        intervals.sort(key=lambda x: x[1])

        k = 0
        end = intervals[0][1]

        for i in range(1, len(intervals)):
            if intervals[i][0] < end:
                k += 1
            else:
                end = intervals[i][1]

        return k

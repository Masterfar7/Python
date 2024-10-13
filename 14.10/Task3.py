"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/array-nesting/
"""


from typing import List

class Solution:
    def arrayNesting(self, nums: List[int]) -> int:
        n = ln(nums)
        visited = [False] * n
        ln = 0

        for i in range(n):
            if not visited[i]:
                ln1 = 0
                ind = i
                while not visited[ind]:
                    visited[ind] = True
                    ind = nums[ind]
                    ln1 += 1

                ln = max(ln, ln1)

        return ln


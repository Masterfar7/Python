"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/ones-and-zeroes/
"""


class Solution(object):
    def findMaxForm(self, strs: list[str], m: int, n: int) -> int:
        a = [[0] * (n + 1) for _ in range(m + 1)]

        for s in strs:
            k0 = s.count('0')
            k1 = s.count('1')

            for i in range(m, k0 - 1, -1):
                for j in range(n, k1 - 1, -1):
                    a[i][j] = max(a[i][j], a[i - k0][j - k1] + 1)

        return a[m][n]

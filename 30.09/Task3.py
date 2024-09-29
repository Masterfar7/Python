"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/multiply-strings/description/
"""


class Solution:
    def longestPalindromeSubseq(self, s: str) -> int:
        n = len(s)
        a = [[0] * n for _ in range(n)]
        for i in range(n):
            a[i][i] = 1
        for length in range(2, n + 1):
            for i in range(n - length + 1):
                j = i + length - 1
                if s[i] == s[j]:
                    a[i][j] = a[i + 1][j - 1] + 2
                else:
                    a[i][j] = max(a[i + 1][j], a[i][j - 1])

        return a[0][n - 1]

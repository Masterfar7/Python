"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/regular-expression-matching/description/
"""


class Solution(object):
    def isMatch(self, s, p):
        a = [[False] * (len(p) + 1) for _ in range(len(s) + 1)]
        a[0][0] = True
        for j in range(1, len(p) + 1):
            if p[j - 1] == '*':
                a[0][j] = a[0][j - 2]
        for i in range(1, len(s) + 1):
            for j in range(1, len(p) + 1):
                if p[j - 1] == s[i - 1] or p[j - 1] == '.':
                    a[i][j] = a[i - 1][j - 1]
                elif p[j - 1] == '*':
                    a[i][j] = a[i][j - 2] or (a[i - 1][j] and (s[i - 1] == p[j - 2] or p[j - 2] == '.'))
        return a[len(s)][len(p)]

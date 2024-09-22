"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/generate-parentheses/description/
"""


class Solution(object):
    def generateParenthesis(self, n):
        res = []
        def bt(st1, k, k1):
            if len(st1) == 2 * n:
                res.append(st1)
                return
            if k < n:
                bt(st1 + "(", k + 1, k1)
            if k1 < k:
                bt(st1 + ")", k, k1 + 1)
        bt("", 0, 0)
        return res
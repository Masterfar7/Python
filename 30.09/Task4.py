"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/next-greater-element-iii/submissions/
"""


class Solution(object):
    def nextGreaterElement(self, n: int) -> int:
        lst = list(str(n))
        i = len(lst) - 2

        while i >= 0 and lst[i] >= lst[i + 1]:
            i -= 1

        if i == -1:
            return -1

        j = len(lst) - 1

        while lst[j] <= lst[i]:
            j -= 1

        lst[i], lst[j] = lst[j], lst[i]
        lst = lst[:i + 1] + lst[i + 1:][::-1]
        res = int(''.join(lst))

        if res > 2 ** 31 - 1:
            return -1

        return res


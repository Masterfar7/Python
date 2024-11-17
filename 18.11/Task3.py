"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/permutation-in-string/description/
"""


from collections import Counter


class Solution:
    def checkInclusion(self, s1: str, s2: str) -> bool:
        len_s1, len_s2 = len(s1), len(s2)

        if len_s1 > len_s2:
            return False

        s1c = Counter(s1)
        s2c = Counter(s2[:len_s1])

        if s1c == s2c:
            return True

        for i in range(len_s1, len_s2):
            s2c[s2[i]] += 1
            s2c[s2[i - len_s1]] -= 1

            if s2c[s2[i - len_s1]] == 0:
                del s2c[s2[i - len_s1]]

            if s1c == s2c:
                return True

        return False



"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/replace-the-substring-for-balanced-string/description/
"""


from collections import Counter

class Solution(object):
    def balancedString(self, s):
        n = len(s)
        tg = n // 4
        count = Counter(s)
        e = {ch: max(0, count[ch] - tg) for ch in "QWER"}

        if sum(e.values()) == 0:
            return 0

        l = 0
        mn = n

        for r in range(n):
            if s[r] in e:
                e[s[r]] -= 1

            while all(e[ch] <= 0 for ch in "QWER"):
                mn = min(mn, r - l + 1)
                if s[l] in e:
                    e[s[l]] += 1
                l += 1

        return mn


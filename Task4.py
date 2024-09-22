"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-palindromic-substring/description/
"""


class Solution(object):
    def longestPalindrome(self, s):
        def centre(s, l, r):
            while l >= 0 and r < len(s) and s[l] == s[r]:
                l -= 1
                r += 1
            return r - l - 1
            if len(s) < 1:
                return ""

        st, end = 0, 0
        for i in range(len(s)):
            len1 = centre(s, i, i)
            len2 = centre(s, i, i + 1)
            mx = max(len1, len2)

            if mx > end - st:
                st = i - (mx - 1) // 2
                end = i + mx // 2
        return s[st:end + 1]

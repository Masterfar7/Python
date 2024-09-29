"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/longest-substring-without-repeating-characters/description/
"""


class Solution(object):
    def lengthOfLongestSubstring(self, s):
        st = set()
        l = 0
        mx = 0
        for r in range(len(s)):
            while s[r] in st:
                st.remove(s[l])
                l += 1
            st.add(s[r])
            mx = max(mx, r - l + 1)
        return mx

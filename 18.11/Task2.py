"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
"""


class Solution:
    def longestSubstring(self, s: str, k: int) -> int:
        mx = 0
        n = len(s)

        for uc in range(1, 27):
            ch = [0] * 26
            st = 0
            end = 0
            u = 0
            k = 0

            while end < n:
                if u <= uc:
                    idx = ord(s[end]) - ord("a")
                    if ch[idx] == 0:
                        u += 1
                    ch[idx] += 1
                    if ch[idx] == k:
                        k += 1
                    end += 1
                else:
                    idx = ord(s[st]) - ord("a")
                    if ch[idx] == k:
                        k -= 1
                    ch[idx] -= 1
                    if ch[idx] == 0:
                        u -= 1
                    st += 1

                if u == uc and u == k:
                    mx = max(mx, end - st)

        return mx
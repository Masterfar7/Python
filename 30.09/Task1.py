"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/remove-duplicate-letters/
"""


class Solution(object):
    def removeDuplicateLetters(self, s: str) -> str:
        ind = {}
        for i in range(len(s)):
            ind[s[i]] = i

        st = []
        stk = set()

        for i in range(len(s)):
            ch = s[i]
            if ch in stk:
                continue

            while st and st[-1] > ch and i < ind[st[-1]]:
                rch = st.pop()
                stk.remove(rch)

            st.append(ch)
            stk.add(ch)

        return "".join(st)

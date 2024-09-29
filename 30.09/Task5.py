"""
leetcode.com/problem-list/string/
url: https://leetcode.com/problems/regular-expression-matching/description/
"""


class Solution(object):
    def scoreOfParentheses(self, s: str) -> int:
        st = []
        for ch in s:
            if ch == '(':
                st.append(0)
            else:
                top = st.pop()
                sc = 1 if top == 0 else 2 * top
                if st:
                    st[-1] += sc
                else:
                    st.append(sc)

        return st[0]


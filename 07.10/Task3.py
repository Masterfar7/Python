"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/daily-temperatures/
"""


from typing import List

class Solution:
    def dailyTemperatures(self, temp: List[int]) -> List[int]:
        n = len(temp)
        ans = [0] * n
        st = []
        for i in range(n):
            while st and temp[i] > temp[st[-1]]:
                ind = st.pop()
                ans[ind] = i - ind
            st.append(i)

        return ans


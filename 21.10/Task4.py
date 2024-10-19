"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/open-the-lock/
"""


from collections import deque
from typing import List

class Solution:
    def openLock(self, deadends: List[str], target: str) -> int:
        a = set(deadends)
        if "0000" in a:
            return -1

        q = deque([("0000", 0)])
        visited = set("0000")

        while q:
            cur, t = q.popleft()

            if cur == tar:
                return t
            for i in range(4):
                for move in [-1, 1]:
                    nx = (int(cur[i]) + move) % 10
                    nx1 = cur[:i] + str(nx) + cur[i + 1:]

                    if nx1 not in visited and nx1 not in a:
                        visited.add(nx1)
                        q.append((nx1, t + 1))

        return -1


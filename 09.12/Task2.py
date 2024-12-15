"""
https://leetcode.com/problem-list/sliding-window/?difficulty=MEDIUM
URL: https://leetcode.com/problems/binary-tree-level-order-traversal-ii/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM
"""

from collections import deque
from typing import List, Optional


class TreeNode:
    def __init__(self, val=0, l=None, r=None):
        self.val = val
        self.left = l
        self.right = r


class Solution:
    def levelOrderBottom(self, root: Optional[TreeNode]) -> List[List[int]]:
        if not root:
            return []

        res = []
        q = deque([root])

        while q:
            level = []
            level_length = len(q)

            for _ in range(level_length):
                node = q.popleft()
                level.append(node.val)

                if node.left:
                    q.append(node.left)
                if node.right:
                    q.append(node.right)

            res.append(level)

        return res[::-1]

"""
https://leetcode.com/problem-list/sliding-window/?difficulty=MEDIUM
URL: https://leetcode.com/problems/path-sum-iii/?envType=problem-list-v2&envId=binary-tree&difficulty=MEDIUM
"""

from collections import defaultdict
from typing import Optional


class TreeNode:
    def __init__(self, val=0, l=None, r=None):
        self.val = val
        self.left = l
        self.right = r


class Solution:
    def pathSum(self, root: Optional[TreeNode], targetSum: int) -> int:
        def dfs(node, sum):
            if not node:
                return 0

            sum += node.val

            k = prefix_sums[sum - targetSum]

            prefix_sums[sum] += 1

            k += dfs(node.left, sum)
            k += dfs(node.right, sum)

            prefix_sums[sum] -= 1

            return k

        prefix_sums = defaultdict(int)
        prefix_sums[0] = 1

        return dfs(root, 0)

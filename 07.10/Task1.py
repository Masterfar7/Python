"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/find-all-duplicates-in-an-array
"""


from typing import List

class Solution:
    def findDuplicates(self, nums: List[int]) -> List[int]:
        dub = []
        for num in nums:
            ind = abs(num) - 1
            if nums[ind] < 0:
                dub.append(abs(num))
            else:
                nums[ind] = -nums[ind]
        return dub


"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/heaters/
"""


from collections import Counter
from typing import List

class Solution:
    def wordSubsets(self, words1: List[str], words2: List[str]) -> List[str]:
        mx = Counter()

        for word in words2:
            wc = Counter(word)
            for ch, fr in wc.items():
                mx[ch] = max(mx[ch], fr)
        uni = []

        for word in words1:
            wc = Counter(word)
            if all(wc[char] >= freq for char, freq in mx.items()):
                uni.append(word)

        return uni


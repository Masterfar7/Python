"""
https://leetcode.com/problem-list/sliding-window/
url: https://leetcode.com/problems/longest-substring-with-at-least-k-repeating-characters/description/
"""


from typing import List


class Solution:
    def maxConsecutiveAnswers(self, answerKey: str, k: int) -> int:

        answ = 0

        l = 0
        count = 0
        for r in range(len(answerKey)):
            if answerKey[r] == "F":
                count += 1

            while count > k:
                if answerKey[l] == 'F':
                    count -= 1

                l += 1

            answ = max(answ, r - l + 1)

        l = 0
        count = 0
        for r in range(len(answerKey)):
            if answerKey[r] == "T":
                count += 1

            while count > k:
                if answerKey[l] == 'T':
                    count -= 1
                l += 1

            answ = max(answ, r - l + 1)

        return answ
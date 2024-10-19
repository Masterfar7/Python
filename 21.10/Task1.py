"""
https://leetcode.com/problem-list/hash-table/
url: https://leetcode.com/problems/bulls-and-cows/
"""


class Solution:
    def getHint(self, secret: str, guess: str) -> str:
        b = 0
        c = 0

        bc = [0] * 10
        gc = [0] * 10

        for i in range(len(secret)):
            if secret[i] == guess[i]:
                b += 1
            else:
                bc[int(secret[i])] += 1
                gc[int(guess[i])] += 1

        for i in range(10):
            c += min(bc[i], gc[i])

        return "{}A{}B".format(b, c)

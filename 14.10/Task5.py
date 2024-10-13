"""
leetcode.com/problem-list/array/
url: https://leetcode.com/problems/heaters/
"""

from typing import List

class Solution:
    def findRadius(self, houses: List[int], heaters: List[int]) -> int:
        houses.sort()
        heaters.sort()
        max_radius = 0

        for house in houses:
            min_distance = float('inf')

            for heater in heaters:
                distance = abs(heater - house)
                if distance < min_distance:
                    min_distance = distance
                if heater > house:
                    break

            max_radius = max(max_radius, min_distance)

        return max_radius


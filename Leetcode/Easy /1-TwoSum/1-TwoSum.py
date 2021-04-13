
# Leetcode Problem #1
# Two Sum
# https://leetcode.com/problems/two-sum/
# Video: Coming soon


class Solution:
    def twoSum(self, nums: list, target: int) -> list:
        checked = {}
        for k, num in enumerate(nums):
            if (target - num) in checked:
                return [checked[target - num], k]
            checked[num] = k
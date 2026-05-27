# LeetCode #1 - Two Sum
# Difficulty: Easy
# Runtime: 0ms | Beats: 100%
# Pattern: HashMap

class Solution:
    def twoSum(self, nums, target):
        seen = {}
        for i, num in enumerate(nums):
            complement = target - num
            if complement in seen:
                return [seen[complement], i]
            seen[num] = i

# LeetCode #217 - Contains Duplicate
# Difficulty: Easy | Beats: 46.77%
# Pattern: HashSet | Time: O(n) | Space: O(n)

class Solution:
    def containsDuplicate(self, nums: List[int]) -> bool:
        seen = set()
        for num in nums:
            if num in seen:
                return True
            seen.add(num)
        return False

# LeetCode #242 - Valid Anagram
# Difficulty: Easy
# Runtime: 11ms | Beats: 76.73%
# Pattern: HashMap / Character Count

class Solution:
    def isAnagram(self, s: str, t: str) -> bool:
        if len(s) != len(t):
            return False
        
        count = {}
        
        for char in s:
            count[char] = count.get(char, 0) + 1
            
        for char in t:
            count[char] = count.get(char, 0) - 1
            
        return all(val == 0 for val in count.values())

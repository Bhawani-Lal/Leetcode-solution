# LeetCode #125 - Valid Palindrome
# Difficulty: Easy | Beats: 81.24%
# Pattern: Two Pointer | Time: O(n)

class Solution:
    def isPalindrome(self, s: str) -> bool:
        clean = ""
        for ch in s:
            if ch.isalnum():
                clean += ch.lower()
        return clean == clean[::-1]

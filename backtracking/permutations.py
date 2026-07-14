Accepted
26 / 26 testcases passed
bhawani01
bhawani01
submitted at Jul 14, 2026 23:26

Analysis

Solution
Runtime
0
ms
Beats
100.00%
Memory
19.50
MB
Beats
65.27%
Code
Python3
class Solution:
    def permute(self, nums: List[int]) -> List[List[int]]:

        result = []
        current = []
        used = [False] * len(nums)

        def backtrack():

            if len(current) == len(nums):
                result.append(current[:])
                return

            for i in range(len(nums)):

                if used[i]:
                    continue

                current.append(nums[i])
                used[i] = True

                backtrack()

                current.pop()
                used[i] = False

        backtrack()

        return result
        

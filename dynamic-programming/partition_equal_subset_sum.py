from typing import List

class Solution:
    def canPartition(self, nums: List[int]) -> bool:

        total = sum(nums)

        # Odd total cannot be divided equally
        if total % 2 != 0:
            return False

        target = total // 2

        dp = [False] * (target + 1)
        dp[0] = True

        for num in nums:

            for current_sum in range(target, num - 1, -1):

                if dp[current_sum - num]:
                    dp[current_sum] = True

        return dp[target]

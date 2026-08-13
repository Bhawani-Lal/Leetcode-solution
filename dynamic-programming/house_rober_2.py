class Solution:
    def rob(self, nums: List[int]) -> int:
        n = len(nums)

        if n == 1:
            return nums[0]

        def robLinear(houses):

            prev2 = 0
            prev1 = 0

            for money in houses:

                current = max(
                    prev1,
                    money + prev2
                )

                prev2 = prev1
                prev1 = current

            return prev1

        case1 = robLinear(nums[:-1])
        case2 = robLinear(nums[1:])

        return max(case1, case2)

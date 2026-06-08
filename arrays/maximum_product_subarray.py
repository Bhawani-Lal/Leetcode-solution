class Solution:
    def maxProduct(self, nums: List[int]) -> int:

        maxProduct = nums[0]
        minProduct = nums[0]
        answer = nums[0]

        for i in range(1, len(nums)):

            num = nums[i]

            if num < 0:
                maxProduct, minProduct = minProduct, maxProduct

            maxProduct = max(num, maxProduct * num)
            minProduct = min(num, minProduct * num)

            answer = max(answer, maxProduct)

        return answer

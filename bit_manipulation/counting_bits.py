class Solution:
    def countBits(self, n: int) -> List[int]:
        
        answer = []

        for num in range(n +1):
            count = 0
            temp = num

            while temp:
                temp = temp & (temp -1)
                count += 1
            answer.append(count)
        return answer

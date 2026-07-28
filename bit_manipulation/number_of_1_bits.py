class Solution:
    def hammingWeight(self, n: int) -> int:
         count = 0

         while n > 0:
            # Check wheather the last bit is 1 
            if n & 1:
                count +=1
            
            # Remove The last bit 
            n = n >> 1
         return count

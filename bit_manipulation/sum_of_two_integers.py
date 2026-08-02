class Solution:
    def getSum(self, a: int, b: int) -> int:
        
        mask = 0xFFFFFFFF
        max_int = 0x7FFFFFFF
        
        while b & mask:
            carry = ((a & b) << 1) & mask
            a = (a ^ b) & mask
            b = carry
        
        # If result fits in positive 32-bit range, return as is
        if a <= max_int:
            return a
        # Otherwise convert to negative
        else:
            return ~(a ^ mask)

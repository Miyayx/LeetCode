class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        import math
        m = 0
        i = 1
        while n:
            if n%2:
                m += int(math.pow(2, 32-i))
            n = n/2
            i += 1
        return m
        
#Note: the result of math.pow is float

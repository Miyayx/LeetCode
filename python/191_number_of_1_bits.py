class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        count = 0
        while n:
           count += n%2
           n = n/2
        return count 
        

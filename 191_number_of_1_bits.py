class Solution:
    # @param n, an integer
    # @return an integer
    def hammingWeight(self, n):
        ret = 0
        while n>0:
            ret += n & 1
            n = n>>1
        return ret
     

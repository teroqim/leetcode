class Solution:
    # @param n, an integer
    # @return an integer
    def reverseBits(self, n):
        return int(''.join(list(reversed(bin(n)[2:].zfill(32)))), 2)


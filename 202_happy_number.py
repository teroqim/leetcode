class Solution:
    # @param {integer} n
    # @return {boolean}
    def isHappy(self, n):
        limit = 7
        cur = n
        while limit > 0:
            if cur == 1:
                return True
            sum = 0
            d = cur
            while d > 0:
                m = d % 10
                sum += m*m
                d = math.floor(d/10)
                cur = sum
                limit -= 1
            else:
                return False


class Solution:
    # @param {integer} n
    # @return {integer}
    def countPrimes(self, n):
        from math import sqrt
        if n<=2:
            return 0
        #Sieve of Eratosthenes
        numbers = [True]*(n+1)
        numbers[0] = False
        numbers[1] = False
        count = 0
        sq = sqrt(n)
        for i in range(2, n):
            if numbers[i]:
                k = 0
                while i*i + k*i < n:
                    numbers[i*i + k*i] = False
                    k += 1
                    count += 1
        return count


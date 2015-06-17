class Solution:
    # @param {integer[]} nums
    # @return {integer}
    def rob(self, nums):
        le = len(nums)
        if not nums:
            return 0
        if le < 3:
            return max(nums)
        max_right = nums
        for i in range(0, le):
            if le-1-i == le-3:
                max_right[le-1-i] += max_right[le-1]
            if le-1-i < le-3:
                max_right[le-1-i] += max(max_right[le-1-i+2:])

        return max(max_right[0:2])


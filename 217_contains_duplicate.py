class Solution:
    # @param {integer[]} nums
    # @return {boolean}
    def containsDuplicate(self, nums):
        dups = {}
        for val in nums:
            if dups.has_key(val):
                return True
            dups[val] = None
            return False


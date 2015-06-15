class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {boolean}
    def containsNearbyDuplicate(self, nums, k):
        if not nums or k <= 0:
            return False

        dups = {} 
        for i in range(0, len(nums)):
            if dups.has_key(nums[i]):
                if abs(dups[nums[i]] - i) <= k:
                    return True

            dups[nums[i]] = i

        return False


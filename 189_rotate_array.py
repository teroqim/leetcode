class Solution:
    # @param {integer[]} nums
    # @param {integer} k
    # @return {void} Do not return anything, modify nums in-place instead.
    def rotate(self, nums, k):
        steps = k % len(nums)
        nums[:] = nums[-steps:] + nums[:-steps]


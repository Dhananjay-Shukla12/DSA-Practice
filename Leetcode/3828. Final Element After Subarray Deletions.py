class Solution:
    def finalElement(self, nums: List[int]) -> int:
        n = len(nums)
        if nums[0]>=nums[n-1]:
            return nums[0]
        else:
            return nums[n-1]
        
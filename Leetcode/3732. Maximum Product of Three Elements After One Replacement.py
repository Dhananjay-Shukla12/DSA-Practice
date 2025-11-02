class Solution:
    def maxProduct(self, nums: List[int]) -> int:
        for i in range(len(nums)):
            if nums[i]<0:
                nums[i] = nums[i] * (-1)
        
        nums.sort()
        ans = nums[-1]*nums[-2]*100000
        return ans
        
class Solution:
    def evenNumberBitwiseORs(self, nums: List[int]) -> int:
        x = 0
        k = 0
        for i in range(0,len(nums)):
            if nums[i]%2==0:
                x=nums[i]
                k = i
                break
            
        for i in range(k+1,len(nums)):
            if nums[i]%2==0:
                x = x | nums[i]
        return x
    